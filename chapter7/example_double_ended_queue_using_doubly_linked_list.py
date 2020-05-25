"""
based on example_doubly_linked_list, 
accomplish the double-ended-queue ADT
"""

from example_doubly_linked_list import _DoublyLinkedList
from example_doubly_linked_list import Empty

class DoubleEndedQueue(_DoublyLinkedList):
    """double-ended-queue implementation"""

    def first(self):
        if self.is_empty():
            raise Empty("The queue is empty already")
        else:
            actual_head = self._head._next
            return actual_head._element
    
    def last(self):
        if self.is_empty():
            raise Empty("The queue is empty already")
        else:
            actual_trailer = self._trailer._prev
            return actual_trailer._element
    
    def insert_first(self, value):
        self._insert_between(value, self._head, self._head._next)
    
    def insert_last(self, value):
        self._insert_between(value, self._trailer._prev, self._trailer)
    
    def delete_first(self):
        if self.is_empty():
            raise Empty("The queue is empty already")
        else:
            value = self._delete_node(self._head._next)
            return value
    
    def delete_last(self):
        if self.is_empty():
            raise Empty("The queue is empty already")
        else:
            value = self._delete_node(self._trailer._prev)
            return value
    
    def show(self):
        """for debug purpose"""
        if self.is_empty():
            print("Empty queue")
        else:
            print("head <= trail")
            node = self._head._next
            while node != self._trailer:
                print(node._element, end='  ')
                node = node._next
            print()


if __name__ == '__main__':

    q = DoubleEndedQueue()
    print("initially: ")
    q.show()
    print()

    for i in range(20):
        if i % 2 == 0:  q.insert_first(i)
        else:           q.insert_last(i)
    print("insert 20 digits: ")
    q.show()
    print()

    for i in range(5):
        print(q.delete_last())
        print(q.delete_first())
    print("delete last 5 and first 5")
    q.show()
    print()

    print("length: ", len(q))
    print("first ", q.first())
    print("last ", q.last())
