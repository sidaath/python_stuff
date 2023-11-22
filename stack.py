class Item:
    def __init__(self, num):
        self.index = 0
        self.number = num

    def print(self):
        print(self.number)



class LinkedList:
    def __init__(self):
        self.__list = []

    def push(self, Item):
        self.__list.append(Item)

    def print(self):
        for index, item in enumerate(self.__list):
            item.print()


item1 = Item(11)
item2 = Item(222)

X = LinkedList()

X.push(item1)
X.push(item2)

X.print()