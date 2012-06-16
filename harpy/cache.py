class Cache(object):
    def __init__(self, j):
        self.raw = j

        if "beforeRequest" in self.raw:
            self.before_request = CacheRequest(self.raw["beforeRequest"])
        else:
            self.before_request = None

        if "afterRequest" in self.raw:
            self.after_request = CacheRequest(self.raw["afterRequest"])
        else:
            self.after_request = None

        if "comment" in self.raw:
            self.comment = self.raw["comment"]
        else:
            self.comment = ''


class CacheRequest(object):
    def __init__(self, j):
        self.raw = j

        if "expires" in self.raw:
            self.expires = CacheRequest(self.raw["expires"])
        else:
            self.expires = None

        self.last_access = self.raw["lastAccess"]
        self.etag = self.raw["eTag"]
        self.hit_count = self.raw["hitCount"]
        if "comment" in self.raw:
            self.comment = self.raw["comment"]
        else:
            self.comment = ''
