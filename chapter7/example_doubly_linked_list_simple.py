"""
a simple illustration of doubly linked list.
for the question q4
"""

class Node:
    __slots__ = '_element', '_prev', '_next'
    def __init__(self, element, prev, next):
        self._element = element
        self._prev = prev
        self._next = next

class SimpleDoublyLinkedList:
    
    def __init__(self):
        self._head = Node(None, None, None)
        self._trailer = Node(None, None, None)
        self._size = 0
    
        self._head._next = self._trailer
        self._trailer._prev = self._head
    
    def add(self, value):
        # assume add to the last
        new = Node(value, None, None)
        old_actual_tail = self._trailer._prev
        # relink the list
        old_actual_tail._next = new
        new._next = self._trailer

        new._prev = old_actual_tail
        self._trailer._prev = new

        self._size += 1
    
    def show(self):
        # for debug purpose
        if self._size == 0:
            print("Empty linked list")
        else:       # print both the prev and next, to examine the linkness

            print("first <= last use _next")
            node = self._head._next
            while node != self._trailer:
                print(node._element, end='  ')
                node = node._next
            print()

            print("last >= first use _prev")
            node = self._trailer._prev
            while node != self._head:
                print(node._element, end='  ')
                node = node._prev
            print()


if __name__ == '__main__':

    linked = SimpleDoublyLinkedList()
    for i in range(20): linked.add(i)
    
    linked.show()

