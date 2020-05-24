"""
Use two stacks to accomplish queue ADT.
This is a better design then q25.py , so that first and dequeue are O(1) and enqueue is O(n)
"""

from example_stack import ArrayStack
from example_stack import Empty

class ArrayQueueUseTwoStacks_2:
    """
    a better design.
    enqueue: O(n), and then make the first element at the top of the queue.
    dequeue and first: O(1)
    """

    def __init__(self):
        self._a = ArrayStack()
        self._b = ArrayStack()
        self._num = 0
    
    def __len__(self):
        return self._num

    def is_empty(self):
        return self._num == 0

    def first(self):
        return self._a.top()

    def enqueue(self, value):
        # put the new element at the bottom of the stack
        # note that right now self._a has first element at the top of the stack

        self._num += 1

        while not self._a.is_empty():
            self._b.push(self._a.pop())
        
        self._b.push(value)         # this is the new value

        while not self._b.is_empty():
            self._a.push(self._b.pop())
    

    def dequeue(self):
        # return the first value
        
        if self._num == 0:
            raise Empty("queue is empty")
        else:
            self._num -= 1

        return self._a.pop()


if __name__ == '__main__':
    
    q = ArrayQueueUseTwoStacks_2()
    print("initally, check if queue is empty: ", q.is_empty())
    
    print("put 0 to 29 into the queue")
    for i in range(30):     q.enqueue(i)

    print("length of queue: ", len(q))
    print("first value: ", q.first())

    print("dequeue 25 elements")
    for _ in range(25):     print(q.dequeue())

    print("check length: ", len(q))
    print("check first: ", q.first())