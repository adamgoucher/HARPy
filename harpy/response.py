from . import cookie
from . import header
from . import content


class Response(object):
    def __init__(self, j):
        self.raw = j

        self.status = self.raw["status"]
        self.status_text = self.raw["statusText"]
        self.http_version = self.raw["httpVersion"]

        self.cookies = []
        for c in self.raw["cookies"]:
            self.cookies.append(cookie.Cookie(c))

        self.headers = []
        for c in self.raw["headers"]:
            self.headers.append(header.Header(c))

        self.content = content.Content(self.raw["content"])
        # this is technically required but seems some generators are
        # not including it if there wasnt a redirect
        if "redirectUrl" in self.raw:
            self.redirect_url = self.raw["redirectUrl"]
        else:
            self.redirect_url = ''
        self.headers_size = self.raw["headersSize"]
        self.body_size = self.raw["bodySize"]
        if "comment" in self.raw:
            self.comment = self.raw["comment"]
        else:
            self.comment = ''
