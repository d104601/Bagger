class item:
    def __init__(self, name, type, size, frozen):
        self.name = name
        self.type = type
        self.size = size
        self.frozen = frozen

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getSize(self):
        return self.size

    def getFrozen(self):
        return self.frozen
