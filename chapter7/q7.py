"""
implement the rotate for the a singly linked list based queue
without the creation of any new nodes.

i did not write the code of part 7.1.2
so i simply use example_singly_linked_list to demonstrate the queue
"""

from example_singly_linked_list import _Node
from example_singly_linked_list import SinglyLinkedList

class Empty(Exception): pass

class QueueWithRotate(SinglyLinkedList):

    def rotate(self):
        # put the first element to the last
        # the original class does not have a dummy head
        if self.is_empty():
            raise Empty("The queue is already empty")
        
        elif self._size == 1:
            pass    # one element, nothing to do
        
        else:       # at least two elements
            old_head = self._head
            self._head = old_head._next     # no dummy head, reset the head

            node = self._head
            while node._next is not None:
                node = node._next
            
            # find the tail
            node._next = old_head
            old_head._next = None   # new tail


if __name__ == '__main__':
    q = QueueWithRotate()
    for i in range(20):     q.add(i)
    q.show()

    print("5 rotate")
    for _ in range(5):
        q.rotate()
        q.show()


"""
if using the code in 7.1.2, since there are both dummay head and tail,
then the work will be much easier.
but the core part are the same.
pseudo code for code of 7.1.2 will be:

def rotate(self):
    if self.is_empty():
        raise Empty("Empty queue")
    elif self._size == 1:
        pass
    else:
        # _next for the head part
        move_node = self._head._next
        self._head._next = move_node._next

        # _prev for the head part
        move_node._next._prev = self._head

        # _next for the tail part
        old_actual_tail = self._tail._prev
        old_actual_tail._next = move_node
        move._node._next = self._tail

        # _prev for the tail part
        self._tail._prev = move_node
        move_node._prev = old_actual_tail

"""