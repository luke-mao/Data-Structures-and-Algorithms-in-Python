"""
use linked list to accomplish a queue ADT,
store both head and tail pointers
"""

class Empty(Exception): pass

class Node:
    __slots__ = '_element', '_next'
    
    def __init__(self, element, next):
        self._element = element
        self._next = next

class QueueUseLinkedList:
    """a queue using linked list"""
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):      return self._size

    def is_empty(self):     return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("The queue is empty")
        else:
            return self._head._element

    def enqueue(self, value):
        new_tail_node = Node(value, None)           # first build a new node

        if self.is_empty():
            # if this is the first element, then assign to head. note do not write self._head = Node(value, None)
            # since it will build a different node, although the _element values are equal
            # since both head and tail are pointers, they need to point at exactly the same thing !!!                     
            self._head = new_tail_node   
        else:
            self._tail._next = new_tail_node

        self._tail = new_tail_node
        self._size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise Empty("The queue is already empty")
        else:
            # return the head element, and change the head
            result = self._head._element
            self._head = self._head._next
            self._size -= 1

            if self.is_empty():     # if empty queue, remember to fix the tail too.
                self._tail = None

            return result
    
    def show(self):     # just for debug purpose
        if self.is_empty():
            print("Empty queue")
        else:
            print("head => tail")
            node = self._head
            while node is not None:
                print(node._element, end="  ")
                node = node._next
            print()


if __name__ == '__main__':
    q = QueueUseLinkedList()

    for i in range(20):     q.enqueue(i)
    q.show()

    for _ in range(10):     print(q.dequeue())
    print(q.show())
    print("length ", len(q))
    print("first ", q.first())
    print("is empty check: ", q.is_empty())
