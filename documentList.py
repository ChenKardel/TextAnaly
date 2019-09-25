class Doc:
    def __init__(self, _id=None, _language=None, _text=None):
        self.id = _id
        self.language = _language
        self.text = _text

    def to_dict(self):
        d = {}
        if self.id is not None:
            d["id"] = self.id
        if self.language is not None:
            d["language"] = self.language
        if self.text is not None:
            d["text"] = self.text

class DocList:
    def __init__(self, docs=None):
        if docs is None:
            self.docs = []
        else:
            self.docs = docs

    def to_list(self):
        return [doc.to_dict() for doc in self.docs]

