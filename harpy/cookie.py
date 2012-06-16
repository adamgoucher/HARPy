class Cookie(object):
    def __init__(self, j):
        self.raw = j

        self.name = self.raw["name"]
        self.value = self.raw["value"]
        if "path" in self.raw:
            self.path = self.raw["path"]
        else:
            self.path = ''
        if "domain" in self.raw:
            self.domain = self.raw["path"]
        else:
            self.domain = ''
        if "expires" in self.raw:
            self.expires = self.raw["expires"]
        else:
            self.expires = ''
        if "httpOnly" in self.raw:
            self.http_only = self.raw["httpOnly"]
        else:
            self.http_only = ''
        if "secure" in self.raw:
            self.secure = self.raw["secure"]
        else:
            self.secure = ''
        if "comment" in self.raw:
            self.comment = self.raw["comment"]
        else:
            self.comment = ''
