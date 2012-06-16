import os.path
import pytest
import sys


f = os.path.join(os.path.dirname(__file__), "allievi.sssup.it.120601_0_89e253d69250548c5d814019fdd4f1ca.har.json")


def setup_module(module):
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


class TestHar(object):
    def test_parse(self):
        from harpy.har import Har
        p = Har(f)

    def test_missing_har(self):
        from harpy.har import Har
        with pytest.raises(IOError):
            p = Har("monkey")

    def test_browser(self):
        from harpy.har import Har
        h = Har(f)
        name, version, comment = h.browser
        assert(name == "flying monkey")
        assert(version == "1.1.47")
        assert(comment == '')

    def test_version(self):
        from harpy.har import Har
        h = Har(f)
        assert(h.version == "1.1")

    def test_creator(self):
        from harpy.har import Har
        h = Har(f)
        name, version, comment = h.creator
        assert(name == "WebPagetest")
        assert(version == "1.8")
        assert(comment == '')

    def test_pages(self):
        from harpy.har import Har
        h = Har(f)
        assert(len(h.pages) == 1)

    def test_pages_by_id(self):
        from harpy.har import Har
        h = Har(f)
        p = h.page_by_id("page_2_0")
        assert(p.started_date_time == "2012-06-01T16:40:56.000+00:00")
        assert(p.title == "Run 2, First View for http://allievi.sssup.it/")
        on_content_load, on_load, comment = p.timings
        assert(on_content_load == -1)
        assert(on_load == 8996)
        assert(comment == '')

    def test_all_entries(self):
        from harpy.har import Har
        h = Har(f)
        assert(len(h.entries) == 56)

    def test_entires_by_page_one_way(self):
        from harpy.har import Har
        h = Har(f)
        e = h.entries_by_page_ref("page_2_0")
        assert(len(e) == 56)
