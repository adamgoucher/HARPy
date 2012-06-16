class Content(object):
    def __init__(self, j):
        self.raw = j

        self.size = self.raw["size"]
        if "compression" in self.raw:
            self.compression = self.raw["compression"]
        else:
            self.compression = ''
        self.mime_type = self.raw["mimeType"]
        if "text" in self.raw:
            self.text = self.raw["text"]
        else:
            self.text = ''
        if "encoding" in self.raw:
            self.encoding = self.raw["encoding"]
        else:
            self.encoding = ''
        if "comment" in self.raw:
            self.comment = self.raw["comment"]
        else:
            self.comment = ''
