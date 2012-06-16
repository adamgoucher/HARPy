class Timings(object):
    def __init__(self, j):
        self.raw = j

        if "blocked" in self.raw:
            self.blocked = self.raw["blocked"]
        else:
            self.blocked = -1

        if "dns" in self.raw:
            self.dns = self.raw["dns"]
        else:
            self.dns = -1

        if "connect" in self.raw:
            self.connect = self.raw["connect"]
        else:
            self.connect = -1

        self.send = self.raw["send"]
        self.wait = self.raw["wait"]
        self.receive = self.raw["receive"]

        if "ssl" in self.raw:
            self.ssl = self.raw["ssl"]
        else:
            self.ssl = -1

        if "comment" in self.raw:
            self.comment = self.raw["comment"]
        else:
            self.comment = ''
