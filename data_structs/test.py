import unittest
from LinkedList import Item
from LinkedList import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_push(self):
        ll = LinkedList()
        item1 = Item(10)
        item2 = Item(20)
        item3 = Item(30)
        ll.push(item1)
        ll.push(item2)
        ll.push(item3)

        list2 = [item1, item2, item3]

        self.assertListEqual(ll.list, list2, 'Push has failed')

    def test_pop(self):
        ll = LinkedList()
        item1 = Item(10)
        item2 = Item(20)
        item3 = Item(30)

        ll.push(item1)
        ll.push(item2)
        ll.push(item3)

        ll.pop()

        res = [item1, item2]

        self.assertListEqual(ll.list, res, 'Pop has failed')
        

if __name__ == '__main__':
    unittest.main()