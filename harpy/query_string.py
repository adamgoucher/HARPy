class QueryString(object):
    def __init__(self, j):
        self.raw = j

        self.name = self.raw["name"]
        self.value = self.raw["value"]
        if "comment" in self.raw:
            self.comment = self.raw["comment"]
        else:
            self.comment = ''
