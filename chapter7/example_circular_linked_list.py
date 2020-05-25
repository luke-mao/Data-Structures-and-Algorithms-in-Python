"""
a simple implementation of the circular linked list
"""

class Node:
    __slots__ = '_element', '_next'
    def __init__(self, element, next):
        self._element = element
        self._next = next


class CircularLinkedList:
    """simple ADT for circular linked list"""

    def __init__(self):
        self._size = 0
        self._tail = Node(None, None) # use tail, so add all values in the tail

    def is_empty(self): return self._size == 0

    def add(self, value):
        # default add to the tail
        new = Node(value, None)
        
        if self.is_empty():
            self._tail = new
            self._tail._next = self._tail   # cyclic
        else:
            head = self._tail._next
            self._tail._next = new
            new._next = head
            self._tail = new
        
        self._size += 1

    def show(self):
        # for debug purpose
        if self.is_empty():
            print("Empty linked list")
        else:
            print("head => tail => head")
            head = self._tail._next
            while head != self._tail:
                print(head._element, end='  ')
                head = head._next
            print(head._element, end='  ')  # print the tail element
            print(head._next._element, end='  ')    # print the head again
            print()


if  __name__ == '__main__':
    q = CircularLinkedList()
    for i in range(20):     q.add(i)
    q.show()
    


