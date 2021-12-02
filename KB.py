from bag import bag

class KB:
    def __init__(self):
        self.large = []  # list of large items
        self.largeBottle = []  # list of large items with bottle
        self.medium = []  # list of medium items
        self.mediumFrozen = []  # list of medium items with freezer bag
        self.small = []  # list of small items
        self.suggestion = {}  # dictionary for suggestion

    def check_order(self, unbagged, bag):
        for i in bag.items:
            if i in self.suggestion.keys():
                suggestion = self.suggestion.get(i)
                if suggestion not in unbagged.items and suggestion not in bag.items:
                    print("You ordered " + i.getName() + ", but not " + suggestion.getName()+"."
                          , suggestion.getName(), "will be added to bag as suggestion.")
                    bag.addItem(suggestion)

    # function to add items to knowledge base. it will be classified by size
    def addItemRule(self, item):
        size = item.getSize()
        if size == "Large":
            if item.getType() == "Bottle" and item not in self.largeBottle:
                self.largeBottle.append(item)
            elif item not in self.large:
                self.large.append(item)
        elif size == "Medium":
            if item.getFrozen() == True and item not in self.mediumFrozen:
                self.mediumFrozen.append(item)
            elif item not in self.medium:
                self.medium.append(item)
        elif size == "Small" and item not in self.small:
            self.small.append(item)

    # if current bag is full, prepare new bag
    def checkBagSize(self, currentBag, bagList):
        if currentBag.getLarge() >= 6:
            bagList.append(currentBag)
            currentBag = bag()
        elif currentBag.getMedium() >= 11:
            bagList.append(currentBag)
            currentBag = bag()
        elif currentBag.getSmall() >= 16:
            bagList.append(currentBag)
            currentBag = bag()

    def addSuggestion(self, item1, item2):
        self.suggestion[item1] = item2

    def baggingProcess(self, unbagged, bagList):
        currentBag = bag()

        # Bag Large Bottle item first
        for i in unbagged.items:
            if i in self.largeBottle:
                # run check order and bag size check every bagging item step
                self.check_order(unbagged, currentBag)
                self.checkBagSize(currentBag, bagList)
                currentBag.addItem(i)
                currentBag.large += 1

        # Bag other Large items
        for i in unbagged.items:
            if i in self.large:
                self.check_order(unbagged, currentBag)
                self.checkBagSize(currentBag, bagList)
                currentBag.addItem(i)
                currentBag.large += 1

        # Bag Medium Frozen items
        for i in unbagged.items:
            if i in self.mediumFrozen:
                self.check_order(unbagged, currentBag)
                self.checkBagSize(currentBag, bagList)
                currentBag.addItem(i)
                currentBag.medium += 1

        # Bag other Medium items
        for i in unbagged.items:
            if i in self.medium:
                self.check_order(unbagged, currentBag)
                self.checkBagSize(currentBag, bagList)
                currentBag.addItem(i)
                currentBag.medium += 1

        # Bag small items
        for i in unbagged.items:
            if i in self.small:
                self.check_order(unbagged, currentBag)
                self.checkBagSize(currentBag, bagList)
                currentBag.addItem(i)
                currentBag.small += 1
        self.check_order(unbagged, currentBag)

        bagList.append(currentBag)

    # remove item from knowledge base
    def removeItem(self, item):
        if item in self.large:
            self.large.remove(item)
        elif item in self.medium:
            self.medium.remove(item)
        elif item in self.small:
            self.medium.remove(item)

    def printItems(self):
        print("Available large items:")
        for i in range(len(self.largeBottle)):
            print(self.largeBottle[i].getName())
        for i in range(len(self.large)):
            print(self.large[i].getName())
        print("Available medium items:")
        for i in range(len(self.mediumFrozen)):
            print(self.mediumFrozen[i].getName())
        for i in range(len(self.medium)):
            print(self.medium[i].getName())
        print("Available small items:")
        for i in range(len(self.small)):
            print(self.small[i].getName())

