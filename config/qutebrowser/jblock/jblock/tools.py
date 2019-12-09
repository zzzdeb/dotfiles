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


"""Common helper utilities used in many places."""

import re
import collections
import itertools
import functools

class JBlockParseError(ValueError):
    pass

class AnchorTypes():
	"""Ways that a rule can be anchored.

	This is not meant to be used as an enum, but as a bitstring for better performance and memory usage

	"""
	END      = 0x1  # type: int
	START    = 0x2  # type: int
	HOSTNAME = 0x4  # type: int

def domain_variants(domain):
	"""
	>>> list(_domain_variants("foo.bar.example.com"))
	['foo.bar.example.com', 'bar.example.com', 'example.com', 'com']
	>>> list(_domain_variants("example.com"))
	['example.com', 'com']
	>>> list(_domain_variants("localhost"))
	['localhost']
	"""
	while domain:
		yield domain
		domain = domain.partition(".")[-1]

def split_bw(rules):
	return split_iter(rules, lambda r: not r.is_exception)

def split_bw_domain(rules):
	blacklist, whitelist = split_bw(rules)
	return domain_index(blacklist), domain_index(whitelist)

def domain_index(rules):
	result = collections.defaultdict(list)
	for rule in rules:
		domains = rule.options.get('domain', {})
		for domain, required in domains.items():
			if required:
				result[domain].append(rule)
	return dict(result)

def split_iter(iterable, fn):
	"""Generate two iterables from a passed in one, one which passes pred and one which does not."""
	pass_iter, fail_iter = itertools.tee(iterable)
	return list(filter(fn, pass_iter)), list(itertools.filterfalse(fn, fail_iter))


def combined_regex(regexes, flags=re.IGNORECASE):
	"""
	Return a compiled regex combined (using OR) from a list of ``regexes``.
	If there is nothing to combine, None is returned.
	"""
	joined_regexes = "|".join(filter(None, regexes))
	if not joined_regexes:
		return None

	return re.compile(joined_regexes, flags=flags)
