import os.path
import pytest
import sys


f = os.path.join(os.path.dirname(__file__), "allievi.sssup.it.120601_0_89e253d69250548c5d814019fdd4f1ca.har.json")


def setup_module(module):
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


class TestForInteresting(object):
    def setup_method(self, item):
        from harpy.har import Har
        self.parsed = Har(f)
    
    def test_404s(self):
        four_oh_fours = [e for e in self.parsed.entries if e.response.status == 404]
        assert(len(four_oh_fours) == 1)

    def test_unacceptable_duration_page(self):
        unacceptable_duration = [p for p in self.parsed.pages if p.timings[1] > 5000]
        assert(len(unacceptable_duration) == 1)
        
    def test_acceptable_duration_page(self):
        if self.parsed.pages[0].timings[1] < 10000:
            print "BIOJ"
        acceptable_duration = [p for p in self.parsed.pages if p.timings[1] < 10000]
        assert(len(acceptable_duration) == 1)