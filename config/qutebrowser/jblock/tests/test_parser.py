
# This test file was lifted entirely from
# https://github.com/scrapinghub/adblockparser/blob/master/tests/test_parsing.py

# Copyright (c) 2014 ScrapingHub Inc.
# Copyright (c) 2019 Jay Kamat <jaygkamat@gmail.com>

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

import pytest

from jblock import parser, bucket, tools

# examples are from https://adblockplus.org/en/filter-cheatsheet
# and https://adblockplus.org/en/filters
DOCUMENTED_TESTS = {
	"/banner/*/img^": {
		"blocks": [
			"http://example.com/banner/foo/img",
			"http://example.com/banner/foo/bar/img?param",
			"http://example.com/banner//img/foo",
		],
		"doesn't block": [
			"http://example.com/banner/img",
			"http://example.com/banner/foo/imgraph",
			"http://example.com/banner/foo/img.gif",
		]
	},

	"||ads.example.com^": {
		"blocks": [
			"http://ads.example.com/foo.gif",
			"http://server1.ads.example.com/foo.gif",
			"https://ads.example.com:8000/",
		],
		"doesn't block": [
			"http://ads.example.com.ua/foo.gif",
			"http://example.com/redirect/http://ads.example.com/",
		]
	},

	"|http://example.com/|": {
		"blocks": [
			"http://example.com/",
		],
		"doesn't block": [
			"http://example.com/foo.gif",
			"http://example.info/redirect/http://example.com/",
		]
	},

	"swf|": {
		"blocks": ["http://example.com/annoyingflash.swf"],
		"doesn't block": ["http://example.com/swf/index.html"]
	},

	"|http://baddomain.example/": {
		"blocks": ["http://baddomain.example/banner.gif"],
		"doesn't block": ["http://gooddomain.example/analyze?http://baddomain.example"]
	},

	"||example.com/banner.gif": {
		"blocks": [
			"http://example.com/banner.gif",
			"https://example.com/banner.gif",
			"http://www.example.com/banner.gif",
		],
		"doesn't block": [
			"http://badexample.com/banner.gif",
			"http://gooddomain.example/analyze?http://example.com/banner.gif",
		]
	},

	"http://example.com^": {
		"blocks": [
			"http://example.com/",
			"http://example.com:8000/ ",
		],
		"doesn't block": [
			"http://example.com.ar/",
		]
	},

	"^example.com^": {
		"blocks": ["http://example.com:8000/foo.bar?a=12&b=%D1%82%D0%B5%D1%81%D1%82"],
		"doesn't block": []
	},

	"^%D1%82%D0%B5%D1%81%D1%82^": {
		"blocks": ["http://example.com:8000/foo.bar?a=12&b=%D1%82%D0%B5%D1%81%D1%82"],
		"doesn't block": []
	},

	"^foo.bar^": {
		"blocks": ["http://example.com:8000/foo.bar?a=12&b=%D1%82%D0%B5%D1%81%D1%82"],
		"doesn't block": []
	},
}

RULE_EXCEPTION_TESTS = {
	("adv", "@@advice."): {
		"blocks": ["http://example.com/advert.html"],
		"doesn't block": ["http://example.com/advice.html"]
	},
	("@@advice.", "adv"): {
		"blocks": ["http://example.com/advert.html"],
		"doesn't block": ["http://example.com/advice.html"]
	},
	("@@|http://example.com", "@@advice.", "adv", "!foo"): {
		"blocks": [
			"http://examples.com/advert.html"
		],
		"doesn't block": [
			"http://example.com/advice.html",
			"http://example.com/advert.html"
			"http://examples.com/advice.html"
			"http://examples.com/#!foo"
		]
	},
}


RULES_WITH_OPTIONS_TESTS = {
	# rule: url, params, matches?
	"||example.com": [
		("http://example.com", {'third-party': True}, True),
		("http://example2.com", {'third-party': True}, False),
		("http://example.com", {'third-party': False}, True),
	],
	"||example.com^$third-party": [
		("http://example.com", {'third-party': True}, True),
		("http://example2.com", {'third-party': True}, False),
		("http://example.com", {'third-party': False}, False),
	],
	"||example.com^$third-party,~script": [
		("http://example.com", {'third-party': True, 'script': True}, False),
		("http://example.com", {'third-party': True, 'script': False}, True),
		("http://example2.com", {'third-party': True, 'script': False}, False),
		("http://example.com", {'third-party': False, 'script': False}, False),
	],

	"adv$domain=example.com|example.net": [
		("http://example.net/adv", {'domain': 'example.net'}, True),
		("http://somewebsite.com/adv", {'domain': 'example.com'}, True),
		("http://www.example.net/adv", {'domain': 'www.example.net'}, True),
		("http://my.subdomain.example.com/adv", {'domain': 'my.subdomain.example.com'}, True),

		("http://example.com/adv", {'domain': 'badexample.com'}, False),
		("http://example.com/adv", {'domain': 'otherdomain.net'}, False),
		("http://example.net/ad", {'domain': 'example.net'}, False),
	],

	"adv$domain=example.com|~foo.example.com": [
		("http://example.net/adv", {'domain': 'example.com'}, True),
		("http://example.net/adv", {'domain': 'foo.example.com'}, False),
		("http://example.net/adv", {'domain': 'www.foo.example.com'}, False),
	],

	"adv$domain=~example.com|foo.example.com": [
		("http://example.net/adv", {'domain': 'example.com'}, False),
		("http://example.net/adv", {'domain': 'foo.example.com'}, True),
		("http://example.net/adv", {'domain': 'www.foo.example.com'}, True),
	],

	"adv$domain=~example.com": [
		("http://example.net/adv", {'domain': 'otherdomain.com'}, True),
		("http://somewebsite.com/adv", {'domain': 'example.com'}, False),
	],

	"adv$domain=~example.com|~example.net": [
		("http://example.net/adv", {'domain': 'example.net'}, False),
		("http://somewebsite.com/adv", {'domain': 'example.com'}, False),
		("http://www.example.net/adv", {'domain': 'www.example.net'}, False),
		("http://my.subdomain.example.com/adv", {'domain': 'my.subdomain.example.com'}, False),

		("http://example.com/adv", {'domain': 'badexample.com'}, True),
		("http://example.com/adv", {'domain': 'otherdomain.net'}, True),
		("http://example.net/ad", {'domain': 'example.net'}, False),
	],

	"adv$domain=example.com|~example.net": [
		# ~example.net should be ignored here
		("http://example.net/adv", {'domain': 'example.net'}, False),
		("http://somewebsite.com/adv", {'domain': 'example.com'}, True),
		("http://www.example.net/adv", {'domain': 'www.example.net'}, False),
		("http://my.subdomain.example.com/adv", {'domain': 'my.subdomain.example.com'}, True),

		("http://example.com/adv", {'domain': 'badexample.com'}, False),
		("http://example.com/adv", {'domain': 'otherdomain.net'}, False),
		("http://example.net/ad", {'domain': 'example.net'}, False),
	],

	"adv$domain=example.com,~foo.example.com,script": [
		("http://example.net/adv", {'domain': 'example.com', 'script': True}, True),
		("http://example.net/adv", {'domain': 'foo.example.com', 'script': True}, False),
		("http://example.net/adv", {'domain': 'www.foo.example.com', 'script': True}, False),

		("http://example.net/adv", {'domain': 'example.com', 'script': False}, False),
		("http://example.net/adv", {'domain': 'foo.example.com', 'script': False}, False),
		("http://example.net/adv", {'domain': 'www.foo.example.com', 'script': False}, False),
	],

	"$websocket,domain=extratorrent.cc|firstrowau.eu": [
		("http://example.com", {'domain': 'extratorrent.cc', 'websocket': True}, True),
		("http://example.com", {'domain': 'extratorrent.cc', 'websocket': False}, False),
	]
}

MULTIRULES_WITH_OPTIONS_TESTS = {
	# rules: url, params, should_block
	("adv", "@@advice.$~script"): [
		("http://example.com/advice.html", {'script': False}, False),
		("http://example.com/advice.html", {'script': True}, True),
		("http://example.com/advert.html", {'script': False}, True),
		("http://example.com/advert.html", {'script': True}, True),
	],
}

SPLIT_OPTIONS_TESTS = [
    (
        "subdocument,third-party",
        ["subdocument", "third-party"]
    ),
    (
        "object-subrequest,script,domain=~msnbc.msn.com,~www.nbcnews.com",
        ["object-subrequest", "script", "domain=~msnbc.msn.com,~www.nbcnews.com"],
    ),
    (
        "object-subrequest,script,domain=~msnbc.msn.com,~www.nbcnews.com",
        ["object-subrequest", "script", "domain=~msnbc.msn.com,~www.nbcnews.com"],
    ),
    (
        "~document,xbl,domain=~foo,bar,baz,~collapse,domain=foo.xbl|bar",
        ["~document", "xbl", "domain=~foo,bar,baz", "~collapse", "domain=foo.xbl|bar"]
    ),
    (
        "domain=~example.com,foo.example.com,script",
        ["domain=~example.com,foo.example.com", "script"]
    ),
]

DOMAIN_PARSING_TESTS = [
    ("domain=example.com", {'example.com': True}),
    ("domain=example.com|example.net", {
        'example.com': True,
        'example.net': True
    }),
    ("domain=~example.com", {'example.com': False}),
    ("domain=example.com|~foo.example.com", {
        'example.com': True,
        'foo.example.com': False
    }),
    ("domain=~foo.example.com|example.com", {
        'example.com': True,
        'foo.example.com': False
    }),
    ("domain=example.com,example.net", {
        'example.com': True,
        'example.net': True
    }),
    ("domain=example.com|~foo.example.com", {
        'example.com': True,
        'foo.example.com': False
    }),
    ("domain=~msnbc.msn.com,~www.nbcnews.com", {
        'msnbc.msn.com': False,
        'www.nbcnews.com': False
    }),
]

PARSE_OPTIONS_TESTS = [
    ("domain=foo.bar", {}),
    ("+Ads/$~stylesheet", {'stylesheet': False}),
    ("-advertising-$domain=~advertise.bingads.domain.com", {
        "domain": {'advertise.bingads.domain.com': False}
    }),
    (".se/?placement=$script,third-party", {
        'script': True,
        'third-party': True
    }),
    ("||tst.net^$object-subrequest,third-party,domain=domain1.com|domain5.com", {
        'object-subrequest': True,
        'third-party': True,
        'domain': {
            'domain1.com': True,
            'domain5.com': True,
        }
    })
]

@pytest.mark.parametrize(('rule_text', 'results'), DOCUMENTED_TESTS.items())
def test_documented(rule_text, results):
	rule = parser.JBlockRule(rule_text)

	for url in results["blocks"]:
		assert rule.match_url(url)

	for url in results["doesn't block"]:
		assert not rule.match_url(url)

@pytest.mark.parametrize(('rule_text', 'results'), DOCUMENTED_TESTS.items())
def test_documented_examples(rule_text, results):
	rule = parser.JBlockRule(rule_text)
	rules = bucket.JBlockBuckets([rule_text])

	for url in results["blocks"]:
		assert rule.match_url(url)
		assert rules.should_block(url)

	for url in results["doesn't block"]:
		assert not rule.match_url(url)
		assert not rules.should_block(url)


@pytest.mark.parametrize(('rules', 'results'), RULE_EXCEPTION_TESTS.items())
def test_rule_exceptions(rules, results):
	rules = bucket.JBlockBuckets(rules)

	for url in results["blocks"]:
		assert rules.should_block(url)

	for url in results["doesn't block"]:
		assert not rules.should_block(url)


@pytest.mark.parametrize(('rule_text', 'results'), RULES_WITH_OPTIONS_TESTS.items())
def test_rule_with_options(rule_text, results):
	rule = parser.JBlockRule(rule_text)
	rules = bucket.JBlockBuckets([rule_text])

	for url, params, match in results:
		assert rule.match_url(url, params) == match
		assert rules.should_block(url, params) == match


@pytest.mark.parametrize(('rules', 'results'), MULTIRULES_WITH_OPTIONS_TESTS.items())
def test_rules_with_options(rules, results):
	rules = bucket.JBlockBuckets(rules)
	for url, params, should_block in results:
		assert rules.should_block(url, params) == should_block


def test_regex_rules():
	rules = bucket.JBlockBuckets([r"/banner\d+/"])
	assert rules.should_block("banner123")
	assert not rules.should_block("banners")


def test_rules_supported_options():
	rules = bucket.JBlockBuckets(["adv", "@@advice.$~script"])
	assert not rules.should_block("http://example.com/advice.html", {'script': False})

	# exception rule should be discarded if "script" option is not supported
	rules2 = bucket.JBlockBuckets(["adv", "@@advice.$~script"], supported_options=[])
	assert rules2.should_block("http://example.com/advice.html", {'script': False})


def test_rules_instantiation():
	rule = parser.JBlockRule("adv")
	rules = bucket.JBlockBuckets([rule])
	assert rule.match_url("http://example.com/adv")
	assert rules.should_block("http://example.com/adv")


def test_empty_rules():
	rules = bucket.JBlockBuckets(["adv", "", " \t", parser.JBlockRule("adv2")])
	assert len(rules) == 2


def test_empty_regexp_rules():
	with pytest.raises(tools.JBlockParseError):
		bucket.JBlockBuckets(['adv', '/', '//'])


@pytest.mark.parametrize(('text', 'result'), SPLIT_OPTIONS_TESTS)
def test_option_splitting(text, result):
    assert parser.JBlockRule._split_options(text) == result


@pytest.mark.parametrize(('text', 'result'), DOMAIN_PARSING_TESTS)
def test_domain_parsing(text, result):
    assert parser.JBlockRule._parse_domain_option(text) == result


@pytest.mark.parametrize(('text', 'result'), PARSE_OPTIONS_TESTS)
def test_options_extraction(text, result):
    rule = parser.JBlockRule(text)
    assert rule.options == result
