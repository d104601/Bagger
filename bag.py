class bag:
    def __init__(self):
        self.items = []
        self.large = 0
        self.medium = 0
        self.small = 0

    def addItem(self, item):
        self.items.append(item)

    def getLarge(self):
        return self.large

    def getMedium(self):
        return self.medium

    def getSmall(self):
        return self.small

    def reset(self):
        self.items = []