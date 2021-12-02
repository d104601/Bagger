class unbagged:
    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)
