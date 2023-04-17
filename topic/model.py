
class Article(dict):
    def __init__(self):
        self.title = ""
        self.lead = ""
        self.url = ""
        self.content = ""

    def addContent(self, para = ""):
        if len(self.content) > 0:
            self.content += "\n" + para
            return

        self.content += para
        
    def fullContent(self):
        return self.lead + "\n" + self.content.rstrip("\n")

