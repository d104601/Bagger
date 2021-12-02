#main function for testing
from Bagging import bagging
from KB import KB
from item import item

def main():
    bread = item("Bread", "Plastic Bag", "Medium", False)
    glop = item("Glop", "Jar", "Small", False)
    granola = item("Granola", "Cardboard Box", "Large", False)
    iceCream = item("Ice Cream", "Cardboard Carton", "Medium", True)
    pepsi = item("Pepsi", "Bottle", "Large", False)
    chips = item("Potato Chips", "Plastic Bag", "Medium", False)

    kBase = KB()
    kBase.addItemRule(bread)
    kBase.addItemRule(glop)
    kBase.addItemRule(granola)
    kBase.addItemRule(iceCream)
    kBase.addItemRule(chips)
    kBase.addItemRule(pepsi)
    kBase.addSuggestion(chips, pepsi)

    orderList = [bread, iceCream, chips, granola]
    bagging(orderList, kBase)

if __name__ == '__main__':
   main()