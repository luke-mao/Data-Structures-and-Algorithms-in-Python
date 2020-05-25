"""
linked list ADT, a simple one, demonstrate the add
"""

class _Node:
    __slots__ = '_element', '_next'
    
    def __init__(self, element, next):
        self._element = element
        self._next = next


class SinglyLinkedList:
    """singly linked list, no dummy head"""
    
    def __init__(self):
        self._head = None
        self._size = 0
    
    def __len__(self):      return self._size 
    def is_empty(self):     return self._size == 0

    def add(self, value):
        # add to the end of the queue
        new = _Node(value, None)

        if self.is_empty():
            self._head = new
        else:
            node = self._head
            while node._next is not None:
                node = node._next 
            node._next = new
        
        self._size += 1
    
    def show(self): # for debug
        if self.is_empty():
            print("Empty queue")
        else:
            print("head <= trail")
            node = self._head
            while node is not None:
                print(node._element, end='  ')
                node = node._next
            print()
    

if __name__ == '__main__':

    q = SinglyLinkedList()
    for i in range(20):
        q.add(i)
    q.show()

    

        