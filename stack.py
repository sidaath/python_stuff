from LinkedList import LinkedList
from LinkedList import Item

LL = LinkedList()

loop = True

while(loop):
    print("1. Push")
    print("2. Pop")
    print("3. Print Stack")
    print("99. Quit")

    choice = int(input("select option :"))

    match choice:
        case 1:
            val = input("enter int val to push\n")
            x = Item(val)
            LL.push(x)
        
        case 2:
            element = LL.pop()
            print("removed {} from stack".format(element.number))

        case 3:
            LL.print()

        case 99:
            loop = False

        case _:
            print("invalid choice")
        
        