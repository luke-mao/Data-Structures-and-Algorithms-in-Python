"""
give a complete implementation of the queue ADT
using a singly linked list that includes a header sentinel
"""

class Empty(Exception): pass

class QueueUsingSinglyLinkedList:

    class _Node:
        __slots__ = '_element', '_next'
        def __init__(self, element, next):
            self._element = element
            self._next = next

    "***************************************"

    def __init__(self):
        self._head = self._Node(None, None)     # dummy head
        self._size = 0
    
    def is_empty(self):     return self._size == 0
    def __len__(self):      return self._size

    def first(self):
        if self.is_empty():
            raise Empty("The queue is already empty")
        
        first_node = self._head._next 
        return first_node._element
    
    def dequeue(self):
        # dequeue the first node

        if self.is_empty():
            raise Empty("The queue is already empty")
        
        # extract the poped_node and its value
        first_node = self._head._next 
        value = first_node._element 

        if self._size == 1: # only one element
            self._head._next = None
        else:   # more than 1 element
            self._head._next = first_node._next 

        first_node._next = None
        first_node._element = None

        self._size -= 1
        return value
    
    def enqueue(self, value):
        # enqueue: add to the tail
        new_node = self._Node(value, None)

        if self.is_empty():
            self._head._next = new_node
        else:
            node = self._head._next
            while node._next is not None:
                node = node._next
            
            # now the node is at the tail, its _next is None
            node._next = new_node
        
        self._size += 1

    def show(self): # for debug purpose
        if self.is_empty():
            print("Empty queue")
        else:
            print("Queue first <= last")
            node = self._head._next 
            while node is not None:
                print(node._element, end='  ')
                node = node._next
            print()


if __name__ == '__main__':

    q = QueueUsingSinglyLinkedList()
    for i in range(20):
        q.enqueue(i)
    q.show()

    for _ in range(10):
        print(q.dequeue())
    q.show()

    print("length: ", len(q))