class Item:
    def __init__(self, num):
        self.index = 0
        self.number = num

    def print(self):
        print(self.number)

class LinkedList:
    def __init__(self):
        self.list = []

    def push(self, Item):
        self.list.append(Item)
    
    def pop(self):
        val = self.list[-1]
        self.list.pop()
        return val

    def print(self):
        for index, item in enumerate(self.list):
            item.print()
        
    def get_list(self):
        return self.list