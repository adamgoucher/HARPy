from . import cookie
from . import header
from . import query_string


class Request(object):
    def __init__(self, j):
        self.raw = j

        self.method = self.raw["method"]
        self.url = self.raw["url"]
        self.http_version = self.raw["httpVersion"]

        self.cookies = []
        for c in self.raw["cookies"]:
            self.cookies.append(cookie.Cookie(c))

        self.headers = []
        for c in self.raw["headers"]:
            self.headers.append(header.Header(c))

        self.query_string = []
        for qs in self.raw["queryString"]:
            self.query_string.append(query_string.QueryString(qs))

        if "postData" in self.raw:
            self.post_data = self.raw["postData"]
        else:
            self.post_data = {}
        self.headers_size = self.raw["headersSize"]
        self.body_size = self.raw["bodySize"]
        if "comment" in self.raw:
            self.comment = self.raw["comment"]
        else:
            self.comment = ''
