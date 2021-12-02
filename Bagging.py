from unbagged import unbagged

def bagging(orderList, KB):
    baglist = []
    unbag = unbagged()

    for i in orderList:
        unbag.addItem(i)

    KB.baggingProcess(unbag, baglist)
    for i in range(len(baglist)):
        print("Bag", i + 1, ":")
        for j in baglist[i].items:
            print(j.getName())