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

import functools
import tracemalloc

import pytest

from jblock import bucket


class TestEasyList():

	BLOCK_URLS = [
		"https://ade.googlesyndication.com/ddm/activity_ext/dc_pubid=2;dc_exteid=15485807540606947405;met=1;ecn1=1;etm1=0;eid1=11;acvw=sv%3D690%26cb%3Dj%26e%3D0%26nas%3D1%26sdk%3Db%26p%3D80,24,592,934%26tos%3D0,0,0,0,0%26mtos%3D0,0,0,0,0%26mcvt%3D0%26ps%3D958,2639%26scs%3D1920,1080%26bs%3D958,1028%26pt%3D0%26vht%3D0%26mut%3D0%26a%3D1%26ft%3D0%26at%3D0%26as%3D1%26vpt%3D0%26gmm%3D4%26efpf%3D2%26nmt%3D0%26tcm%3D1%26bt%3D0%26pst%3D-1%26dur%3D-1%26vmtime%3D0%26is%3D128%26cs%3D128%26c%3D1%26mc%3D1%26nc%3D1%26mv%3D1%26nv%3D1%26lte%3D1%26ces%26avms%3Dgeo%26qi%3D88448512%26psm%3D1%26psv%3D1%26psfv%3D1%26psa%3D1%26ptlt%3D739%26pngs%3D9,14,15s%26ssb%3D0,0,0,0,0,0,0,0,0,0,0;gv=atos%3D0,0,0,0,0%26amtos%3D0,0,0,0,0%26avt%3D0%26ss%3D0.22%26t%3D1549127079835?",
		"https://www.youtube.com/api/stats/ads?ver=2&ns=1&event=2&device=1&content_v=8vAxdmb-Qkc&el=detailpage&ei=ps1VXPGOC5ankwa7vJmgCQ&devicever=2.20190130&asr=CgBYAXAB&bti=9477942&format=15_2_1&break_type=1&conn=0&cpn=7X1QfKK0uD1FvCMa&lact=1657&m_pos=0&mt=0&p_h=512&p_w=910&rwt=[RWT]&sdkv=h.3.0.0&slot_pos=0&vis=0&vol=100&wt=1549127079899&ad_cpn=LcKizeX11QpW09kt&ad_id=%2C308155796128&ad_len=15000&ad_mt=0&ad_sys=YT%3AAdSense-Viral%2CAdSense-Viral&ad_v=8lc0fMl3MkQ&aqi=ps1VXPfFGY73sgfwnaiwBA&ad_rmp=1&abv=45",
	]

	PASS_URLS = [
		"https://ssl.google-analytics.com/ga.js",
	]


	@pytest.fixture(scope="class")
	def easylist(self):
		with open("tests/data/easylist.txt", "r") as f:
			lines = f.readlines()
		with open("tests/data/easyprivacy.txt", "r") as f:
			lines += f.readlines()
		return lines

	@pytest.fixture(scope="class")
	def ubo_urls(self):
		with open("tests/data/ubo-abp-urls", "r") as f:
			return f.readlines()

	@pytest.fixture(scope="class")
	def easylist_buckets(self, easylist, ubo_urls):
		"A standard, optimized easylist buckets"
		b = bucket.JBlockBuckets(easylist)
		for url in ubo_urls:
			b.should_block(url)
		b.regen_buckets(easylist)
		return b

	@pytest.fixture(scope="class")
	def easylist_buckets_nofreq(self, easylist):
		tracemalloc.start()
		initial_snapshot = tracemalloc.take_snapshot()

		b = bucket.JBlockBuckets(easylist)

		new_snapshot = tracemalloc.take_snapshot()
		tracemalloc.stop()
		top_stats = new_snapshot.compare_to(initial_snapshot, 'lineno')
		top_stats = top_stats[:100]
		top_stats = "\n".join(map(str, top_stats))
		# Remove if you don't like memory stats
		print(top_stats)
		return b

	def test_bulk_bucket_creation(self, easylist, benchmark) -> bucket.JBlockBuckets:
		benchmark(functools.partial(bucket.JBlockBuckets, easylist))

	@pytest.mark.parametrize('token_freq', [False, True])
	def test_benchmark_no_options(self, ubo_urls, token_freq, easylist, easylist_buckets_nofreq, benchmark):
		def _bench():
			for url in ubo_urls:
				easylist_buckets_nofreq.should_block(url)
		if token_freq:
			_bench()
		else:
			benchmark(_bench)
			return

		easylist_buckets_nofreq.regen_buckets(easylist)

		benchmark(_bench)

	# All tests after this will automatically use frequency optimization
	@pytest.mark.parametrize('url_index', range(len(BLOCK_URLS)))
	def test_block(self, url_index, easylist_buckets, benchmark):
		url = TestEasyList.BLOCK_URLS[url_index]
		def _bench_block():
			assert easylist_buckets.should_block(url) is True
		benchmark(_bench_block)

	@pytest.mark.parametrize('url_index', range(len(PASS_URLS)))
	def test_pass(self, url_index, easylist_buckets, benchmark, ubo_urls):
		url = TestEasyList.PASS_URLS[url_index]
		def _bench_block():
			assert easylist_buckets.should_block(url) is False
		benchmark(_bench_block)


	@pytest.mark.skip()
	def test_print_block(self, easylist, easylist_buckets):
		easylist_buckets.regen_buckets(easylist)
		print(easylist_buckets.summary_str())
