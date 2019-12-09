# Copyright (C) 2019  Jay Kamat
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


import pytest

from jblock import token, parser

TOKENS = {
	"https://snowplow.trx.gitlab.net/com.snowplowanalytics.snowplow/tp2":
	{'https', 'snowplow', 'trx', 'gitlab', 'net', 'com', 'snowplowanalytics', 'snowplow', 'tp2'},
	"https://secure.gravatar.com/avatar/8a29de2d7fbed6e86662f066a4f1ca71?s=48&d=identicon":
	{'https', 'secure', 'gravatar', 'com', 'avatar', '8a29de2d7fbed6e86662f066a4f1ca71', '48', 'identicon'},
	"https://assets.gitlab-static.net/assets/webpack/pages.projects.commit.show.9694cec7.ch":
	{'https', 'assets', 'gitlab', 'static', 'net', 'assets', 'webpack', 'pages', 'projects', 'commit', 'show', '9694cec7', 'ch'},
	"https://assets.gitlab-static.net/assets/webpack/runtime.e0be7892.bundle.js":
	{'https', 'assets', 'gitlab', 'static', 'net', 'assets', 'webpack', 'runtime', 'e0be7892', 'bundle', 'js'},
	"https://start.duckduckgo.com/":
	{'https', 'start', 'duckduckgo', 'com'},
	"https://github.com/qutebrowser/qutebrowser":
	{'https', 'github', 'com', 'qutebrowser', 'qutebrowser'},
}

# These patterns are not converted to regexps yet
PATTERN_TOKENS = {
	r"\/watch\?key\=([\da-f]{32}($))": ["watch"],
	r"https?:\/\/s3\.amazonaws\.com\/[0-9a-z]{57}\/((secure\.js|[0-9a-z]{10}))$": ["s3", "amazonaws", "com"],
	r"wp-content\/plugins\/bsa-pro-scripteo": ["content", "plugins", "bsa", "pro"],
	r"""http:\/\/[a-zA-Z0-9]+\.[a-z]+\/.*(?:[!"#$%&'()*+,:;<=>?@\/\^_`{|}~-]).*[a-zA-Z0-9]+/""": [],
	r"/\:\/\/([0-9]{1,3}\.){3}[0-9]{1,3}/": [],
}

GENERIC_TOKENS = {
	r"adv": [],
	r"/adcss/*": ["adcss"],
	r"/adplay.": ["adplay"],
	# cdn/js/ads currently in bad tokens, need to remove it
	r"/cdn-cgi/pe/bag2?r*popads.net": ["cdn", "cgi", "pe", "bag2"],
	r"@@||fastly.net/js/*_ads.$script": ["fastly", "ads"],
}


@pytest.mark.parametrize(('url', 'tokens'), TOKENS.items())
def test_token_basic(url, tokens):
	assert token.TokenConverter.url_to_tokens(url) == tokens


@pytest.mark.parametrize(('pattern', 'tokens'), PATTERN_TOKENS.items())
def test_pattern_token_basic(pattern, tokens):
	re = parser.JBlockRule(pattern).regex
	t = token.TokenConverter.regex_to_tokens(re)
	assert t == tokens


@pytest.mark.parametrize(('pattern', 'tokens'), GENERIC_TOKENS.items())
def test_pattern_token_basic(pattern, tokens):
	t = parser.JBlockRule(pattern).to_tokens()
	assert t == tokens

## Benchmarks

def test_token_str_bench(benchmark):
	benchmark(lambda: list(map(token.TokenConverter.url_to_tokens, TOKENS.keys())))


@pytest.mark.skip()
def test_token_int_bench(benchmark):
	"""Looks like int hashing is slower than re split."""
	benchmark(lambda: list(map(token.TokenConverter.url_to_tokens_int, TOKENS.keys())))


# Bulk tests

@pytest.mark.skip()
def test_bulk_regexp_match():
	tokens = []
	with open("tests/data/easylist.txt") as f:
		for line in f:
			p = parser.JBlockRule(line)
			if not p.matching_supported():
				continue
			r = p.regex
			t = token.TokenConverter.regex_to_tokens(r)
			if not t:
				tokens.append(line)

	print(tokens)
