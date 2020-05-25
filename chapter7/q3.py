"""
describe a recursive algorithm that count the number of nodes
in a singly linked list

method:
similar to the counting of the height of a tree, 
quite simple and straightforward
"""

from example_singly_linked_list import SinglyLinkedList

def count(node):
    """give the head element, count the number"""

    if node is None:
        return 0
    else:
        return 1 + count(node._next)


if __name__ =='__main__':

    list1 = SinglyLinkedList()
    for i in range(5):  list1.add(i)
    print("length: ", count(list1._head))

    list2 = SinglyLinkedList()
    for i in range(20):  list2.add(i)
    print("length: ", count(list2._head))

    list3 = SinglyLinkedList()
    list3.add(1)
    print("length: ", count(list3._head))

    list4 = SinglyLinkedList()
    print("length: ", count(list4._head))

