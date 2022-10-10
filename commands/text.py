import sys


class Text:
    def __init__(self, attr):
        self.type = "text"
        self.name = attr['name']
        self.action = attr['action']
        self.content = attr['content']

    def item(self):
        return self.name

    def value(self):
        return self.content

    def info(self):
        return {"name": self.name, "action": self.action, "type": self.type}

    def save(self):
        return f'"{self.type}", "{self.name}", "{self.action}", "{self.content}"'


sys.modules[__name__] = Text
