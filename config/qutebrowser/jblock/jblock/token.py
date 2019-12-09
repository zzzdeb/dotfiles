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


import re
import typing
import itertools
import functools
import operator

Token = str


class TokenConverter():
	"""Static class for housing token conversion methods.

	There are two (obvious) options for token format, a substring of the literal token, and an int representing the sum of all the chars in the token.

	Int is preferred for faster dict lookup, but requires loops which are expensive in cpython."""

	VALID_TOKEN_CHARS = frozenset('0123456789%abcdefghijklmnopqrstuvwxyz')
	VALID_TOKEN_CHARS_INT = frozenset(map(ord, VALID_TOKEN_CHARS))
	VALID_TOKEN_CHAR_RE = re.compile(r'[0-9a-z%]{2,}')

	REGEX_TOKEN_RE = re.compile(r'[%0-9A-Za-z]{2,}')
	# If we match this from start of the string, all hope is lost for this token and the rest
	REGEX_TOKEN_ABORT = re.compile(r'[([]')
	# TODO find out if this blocks the case where we do *pattern
	REGEX_BAD_PREFIX = re.compile(r'(^|[^\\]\.|[*?{}\\])$')
	REGEX_BAD_SUFFIX = re.compile(r'^([^\\]\.|\\[dw]|[([{}?*]|$)')
	# These tokens won't interfere with proper matching, they just slow us down.
	# This needs to be automatically generated, this is not good.
	BAD_TOKENS = frozenset(
		['com', 'http', 'https', 'icon', 'images', 'img',
		 'js', 'net', 'news', 'www'])

	HOSTNAME_TOKEN = re.compile(r'[0-9a-z]{2,}')

	REGEX_GOOD_TOKEN = re.compile('[%0-9a-z]{2,}')

	@staticmethod
	def url_to_tokens(s: str) -> typing.Iterable[Token]:
		"""Convert a URL to a list of tokens.

		This is in the critical path, so we need to do as little python as possible ;)

		Converting the list -> set seems painful (+3us), but avoids pathological cases (eg: a bunch of 'ads' tokens over
		and over).

		Using an iterator seems to be slower due to the needed conversion (.group)
		"""
		return set(TokenConverter.VALID_TOKEN_CHAR_RE.findall(s.lower()))

	@staticmethod
	def url_to_tokens_int(s: str) -> typing.MutableSet[int]:
		"""Alternative int token generation.

		Seems to be 2x slower than the re based solution on cpython, but 4x faster than the re based solution on pypy.

		Based on this absolute mess:
		https://github.com/gorhill/uBlock/blob/261ef8c510fd91ead57948d1f7793a7a5e2a25fd/src/js/utils.js#L81
		"""
		tally, tokens, arr = 0, set(), bytearray(s, 'ascii')
		for char in arr:
			if char in TokenConverter.VALID_TOKEN_CHARS_INT:
				tally += char
			else:
				tokens.add(tally)
				tally = 0
		return tokens

	# Alternative generator based implementation
	# @staticmethod
	# def url_to_tokens_int(s: str) -> typing.MutableSet[int]:
	# 	tokens, arr = set(), bytearray(s, 'ascii')
	# 	groups = itertools.groupby(arr, TokenConverter.VALID_TOKEN_CHARS_INT.__contains__)
	# 	groups = filter(operator.itemgetter(0), groups)
	# 	groups = list(map(itertools.accumulate, map(operator.itemgetter(1), groups))j
	# 	return groups

	@staticmethod
	def str_token_to_int(s: str) -> typing.Iterator[int]:
		"""Convert a string-based token into an int based token."""
		return itertools.accumulate(bytearray(s, 'ascii'))


	@staticmethod
	def regex_to_tokens(s: str) -> typing.MutableSequence[Token]:
		"""Convert a regex to tokens, if possible.

		https://github.com/gorhill/uBlock/blob/4f3aed6fe6347572c38ec9a293f933387b81e5de/src/js/static-net-filtering.js#L1921
		"""
		tokens = []  # type: typing.List[Token]
		for match in TokenConverter.REGEX_TOKEN_RE.finditer(s):
			# prefix is from the start of the string to the start of the match
			prefix = s[0:match.start(0)]
			suffix = s[match.end(0):]
			match_str = match.group(0).lower()

			# If we have any of these characters leading to our match, we cannot reliably get a substring (this token
			# could be in an optional match or char class)
			if TokenConverter.REGEX_TOKEN_ABORT.search(prefix):
				return tokens

			if (TokenConverter.REGEX_BAD_PREFIX.search(prefix) or
				TokenConverter.REGEX_BAD_SUFFIX.search(suffix)):
				# This token is unsuitable.
				continue

			tokens.append(match_str)

		return tokens

	@staticmethod
	def hostname_match_to_tokens(s: str) -> typing.MutableSequence[Token]:
		"""Assume we have a hostname anchored rule, find all matches.
		Assumes no wildcards at all."""
		return TokenConverter.HOSTNAME_TOKEN.findall(s.lower())

	@staticmethod
	def generic_filter_to_tokens(
			s: str, allow_left: bool, allow_right: bool) -> typing.MutableSequence[Token]:
		"""Convert a generic filter to tokens

		https://github.com/gorhill/uBlock/blob/4f3aed6fe6347572c38ec9a293f933387b81e5de/src/js/static-net-filtering.js#L1895

		allow_left/allow_right control if we are allowed to get tokens on the hard left/right (need anchors)

		"""
		bad_tks = []  # type: typing.List[Token]
		tks = []  # type: typing.List[Token]
		for i in TokenConverter.REGEX_GOOD_TOKEN.finditer(s.lower()):
			# If we match *TOKEN* then we have to throw it out, since we only match the largest match.
			if i.start(0) > 0 and s[i.start(0) - 1] == '*':
				continue
			if i.end(0) < len(s) - 1 and s[i.end(0)] == '*':
				continue
			if i.end(0) >= len(s) and not allow_right:
				continue
			if i.start(0) == 0 and not allow_left:
				continue
			token = i.group(0)
			if token not in TokenConverter.BAD_TOKENS:
				tks.append(token)
			else:
				bad_tks.append(token)
		return tks or bad_tks
