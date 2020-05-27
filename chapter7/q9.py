"""
fast algorithm for concatenating two doubly linked list L and M into L'.
so only L is changed, M is unchanged
"""

from example_doubly_linked_list_simple import SimpleDoublyLinkedList
from example_doubly_linked_list_simple import Node

def concatenate(a:SimpleDoublyLinkedList, b:SimpleDoublyLinkedList):
    a._trailer._prev._next = b._head._next
    b._head._next._prev = a._trailer._prev
    a._trailer = b._trailer


if __name__ == '__main__':

    q1 = SimpleDoublyLinkedList()
    for i in range(10):     q1.add(i)
    q1.show()
    print()

    q2 = SimpleDoublyLinkedList()
    for i in range(20, 30):     q2.add(i)
    q2.show()
    print()

    concatenate(q1, q2)
    q1.show()

"""
hard to copy the whole linked list, 
so the concatenate will destroy the q2
"""
