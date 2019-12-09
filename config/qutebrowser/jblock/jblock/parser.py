# Copyright (C) 2019  Jay Kamat <jaygkamat@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

## Some parts of this file were adapted from scrapinghub/adblockparser.
# Their copyright is reproduced below.
# Copyright (c) 2014 ScrapingHub Inc.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


import re
import typing
import itertools
import functools
import collections
import enum

from jblock.tools import AnchorTypes
from jblock import token, tools
import jblock.matcher


class JBlockRule():
	"""An individual rule which a URL can be matched against."""
	OPTIONS = frozenset({
		"script",
		"image",
		"stylesheet",
		"object",
		"xmlhttprequest",
		"object-subrequest",
		"subdocument",
		"document",
		"elemhide",
		"other",
		"background",
		"xbl",
		"ping",
		"dtd",
		"media",
		"third-party",
		"match-case",
		"collapse",
		"donottrack",
		"websocket",
		# domain is a special case!
		"domain",})

	DROPPED_OPTIONS = set("match-case")

	OPTIONS_SPLIT_RE = re.compile(',(?=~?(?:%s))' % ('|'.join(OPTIONS)))

	__slots__ = [
		'rule_text', 'is_comment', 'is_html_rule',
		'is_exception', 'options', 'matcher',
		'anchors']  # type: typing.List[str]

	def __init__(self, raw_text: str) -> None:
		self.rule_text = raw_text.strip()
		self.is_comment = not raw_text or raw_text.startswith(('!', '[Adblock'))

		if self.is_comment:
			self.is_html_rule = self.is_exception = False
		else:
			# should we use single pound here too?
			self.is_html_rule = '##' in self.rule_text or '#@#' in self.rule_text or '#?#' in self.rule_text
			self.is_exception = self.rule_text.startswith('@@')
			if self.is_exception:
				self.rule_text = self.rule_text[2:]

		if not self.is_comment and '$' in self.rule_text:
			self.rule_text, options_text = self.rule_text.rsplit('$', 1)
			self.options = dict(
				self._parse_option(opt) for opt in self._split_options(options_text)
				# Drop some options if we can't handle them
				if opt not in JBlockRule.DROPPED_OPTIONS)

		else:
			self.options = {}

		# Set up anchoring
		self.anchors = 0  #  type: int
		if self.rule_text:
			if self.rule_text[-1] == '|':
				self.anchors |= AnchorTypes.END
				self.rule_text = self.rule_text[:-1]
			# || in the beginning means beginning of the domain name
			if self.rule_text[:2] == '||':
				self.anchors |= AnchorTypes.HOSTNAME
				self.rule_text = self.rule_text[2:]
			elif self.rule_text[0] == '|':
				# | in the beginning means start of the address
				self.anchors |= AnchorTypes.START
				self.rule_text = self.rule_text[1:]

		# Check if rule is regexp
		is_regex = False
		if self.rule_text.startswith('/') and self.rule_text.endswith('/'):
			if len(self.rule_text) > 1:
				is_regex = True
				self.rule_text = self.rule_text[1:-1]
			else: raise tools.JBlockParseError(
					'Error parsing rule "{}"'.format(self.rule_text))

		# Remove un-needed leading/trailing '*' on non-regexp rules
		if not is_regex and self.rule_text.startswith('*'):
			# The reason for the extra match is that we can't remove the * in some cases:
			# https://github.com/gorhill/uBlock/issues/1669#issuecomment-224822448
			self.rule_text = re.sub(r'^\*+([^%0-9a-zA-Z])', r'\1', self.rule_text)
			# Not 100% sure if we can remove the anchors, but since
			# ubo does it we're leaving performance on the table otherwise.
			self.anchors &= ~(AnchorTypes.HOSTNAME | AnchorTypes.START)
		if not is_regex and self.rule_text.endswith('*'):
			self.rule_text = re.sub(r'([^%0-9a-zA-Z])\*+$', r'\1', self.rule_text)
			self.anchors &= ~AnchorTypes.END

		if self.is_comment or self.is_html_rule:
			# TODO: add support for HTML rules.
			# We should split the rule into URL and HTML parts,
			# convert URL part to a regex and parse the HTML part.
			self.matcher = jblock.matcher.AlwaysTrueMatcher()  # type: jblock.matcher.Matcher
		else:
			self.matcher = jblock.matcher.gen_matcher(self.rule_text, self.anchors, is_regex)

	@classmethod
	def _split_options(cls, options_text):
		return cls.OPTIONS_SPLIT_RE.split(options_text)

	@classmethod
	def _parse_domain_option(cls, text):
		domains = text[len('domain='):]
		parts = domains.replace(',', '|').split('|')
		return dict(map(cls._parse_option_negation, parts))

	@classmethod
	def _parse_option_negation(cls, text):
		return (text.lstrip('~'), not text.startswith('~'))

	@classmethod
	def _parse_option(cls, text):
		if text.startswith("domain="):
			return ("domain", cls._parse_domain_option(text))
		return cls._parse_option_negation(text)

	def is_regex(self):
		return isinstance(self.matcher, jblock.matcher.RegexMatcher)

	def to_tokens(self) -> typing.MutableSequence[token.Token]:
		"""Convert rule to tokens as well as possible.

		https://github.com/gorhill/uBlock/blob/4f3aed6fe6347572c38ec9a293f933387b81e5de/src/js/static-net-filtering.js#L1949

		"""
		if not self.matching_supported(JBlockRule.OPTIONS):
			return []
		if self.is_regex():
			return token.TokenConverter.regex_to_tokens(self.rule_text[1:-1])
		# TODO support '*' regex?

		if AnchorTypes.HOSTNAME & self.anchors and '*' not in self.rule_text:
			return token.TokenConverter.hostname_match_to_tokens(self.rule_text)
		return token.TokenConverter.generic_filter_to_tokens(
			self.rule_text,
			bool((AnchorTypes.START | AnchorTypes.HOSTNAME) & self.anchors),
			bool(AnchorTypes.END & self.anchors))

	def _domain_matches(self, d):
		domain_rules = self.options['domain']
		for d in tools.domain_variants(d):
			if d in domain_rules:
				return domain_rules[d]
		return not any(domain_rules.values())

	def match_url(self, url, options=frozenset(), *, ignore_domain=False):
		"""
		Return if this rule matches the URL.

		ignore_domain: if we shoudn't do any domain checking (assuming it happened before already)
		"""
		return self.match_url_fast(url, options, ignore_domain)

	def match_url_fast(self, url, options, ignore_domain):
		"""Faster version of match_url which does not handle optional arguments"""
		for optname in self.options:
			if optname == 'match-case':  # TODO implement match-case
				continue

			if optname not in options:
				return False
				# raise ValueError("Rule requires option %s" % optname)

			if optname == 'domain':
				if ignore_domain:
					continue
				if not self._domain_matches(options['domain']):
					return False
				continue

			if options[optname] != self.options[optname]:
				return False

		return self.matcher.hit(url)

	def matching_supported(self, options: typing.Union[typing.Dict[str, bool], typing.AbstractSet[str]] = None) -> bool:
		"""Check if we support this rule."""
		if self.is_comment:
			return False

		if self.is_html_rule:  # TODO should we support element hiding rules at all?
			return False

		options = options or set()
		if isinstance(options, dict):
			options = set(options.keys())

		# AbstractSet dosen't have superset, but all it's implementations in the stdlib do.
		if not options.issuperset(self.options.keys()):  # type: ignore
			# some of the required options are not given
			return False

		return True
