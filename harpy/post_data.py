class PostData(object):
    def __init__(self, j):
        self.raw = j

        self.mime_type = self.raw["mimeType"]
        self.params = params.Params(self.raw["params"])
        self.text = self.raw["text"]
        if "comment" in self.raw:
            self.comment = self.raw["comment"]
        else:
            self.comment = ''


class Params(object):
    def __init__(self, j):
        self.raw = j

        self.name = self.raw["name"]
        if "value" in self.raw:
            self.value = self.raw["value"]
        else:
            self.value = ''
        if "fileName" in self.raw:
            self.file_name = self.raw["fileName"]
        else:
            self.file_name = ''
        if "contentType" in self.raw:
            self.content_type = self.raw["contentType"]
        else:
            self.content_type = ''
        if "comment" in self.raw:
            self.comment = self.raw["comment"]
        else:
            self.comment = ''
