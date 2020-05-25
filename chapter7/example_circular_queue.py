"""
circular queue, the tail_next points to the head,
only use two properties: self._next and self._size
"""

class Empty(Exception): pass

class Node:
    __slots__ = '_element', '_next'
    def __init__(self, element, next):
        self._element = element
        self._next = next
    
class CircularQueue:
    """FIFO circular queue"""
    
    def __init__(self):
        # only use the two following properties
        self._tail = None   # self._tail._next = head
        self._size = 0
    
    def is_empty(self):     return self._size == 0
    def __len__(self):      return self._size
    
    def first(self):
        if self.is_empty():
            raise Empty("The queue is already empty")

        head = self._tail._next
        return head._element
    
    def enqueue(self, value):
        new_node = Node(value, None)    # the new node will be the tail

        if self.is_empty():
            # circular queue, link to itself
            new_node._next = new_node
        
        else:
            new_node._next = self._tail._next
            self._tail._next = new_node
        
        self._tail = new_node
        self._size += 1
    
    def dequeue(self):
        # FIFO, need to modify the head
        if self.is_empty():
            raise Empty("The queue is already empty")
        
        head = self._tail._next 
        result = head._element
        self._tail._next = head._next
        self._size -= 1

        if self.is_empty():         # if the last element is removed in this turn, fix the tail
            self._tail = None
        
        return result
    
    def show(self):
        # just for debug purpose
        if self.is_empty():
            print("Empty queue")
        else:
            print("queue head <= tail")
            head = self._tail._next
            while head != self._tail:
                print(head._element, end='  ')
                head = head._next
            print(head._element)        # the printing finish when reach the tail, but still need to print the tail
    
    def rotate(self):
        # rotate the head to the tail
        if not self.is_empty(): # if not empty, if empty not necessary to trigger the Empty Exception
            # the queue is already cyclic, so simply name self._tail = old_head = self._tail._next is enough
            self._tail = self._tail._next


if __name__ == '__main__':
    cq = CircularQueue()

    for i in range(20):     cq.enqueue(i)
    cq.show()

    print("rotate twice")
    cq.rotate()
    cq.show()

    cq.rotate()
    cq.show()

    for _ in range(20):
        print("dequeue: ", cq.dequeue())
        cq.show()
        print()

    print("length ", len(cq))
    print("is empty: ", cq.is_empty())
    
    
    # print(cq.first())

        