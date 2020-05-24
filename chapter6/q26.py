"""
use one douible-ended-queue to accomplish features of queue ADT.
time complexity:
first: O(1)
enqueue: O(1)
dequeue: O(1)
"""

from example_double_ended_queue import ArrayDoubleEndedQueue
from example_double_ended_queue import Empty

class ArrayQueueUseDeque:

    def __init__(self):
        self._a = ArrayDoubleEndedQueue()
        self._num = 0
    
    def __len__(self):
        return self._num
    
    def is_empty(self):
        return self._num == 0
    
    def first(self):
        return self._a.first()
    
    def enqueue(self, value):
        self._num += 1
        return self._a.add_last(value)
    
    def dequeue(self):
        self._num -= 1
        return self._a.delete_first()
    

if  __name__ == '__main__':
    q = ArrayQueueUseDeque()
    print("initally, check if queue is empty: ", q.is_empty())
    
    print("put 0 to 29 into the queue")
    for i in range(30):     q.enqueue(i)

    print("length of queue: ", len(q))
    print("first value: ", q.first())

    print("dequeue 25 elements")
    for _ in range(25):     print(q.dequeue())

    print("check length: ", len(q))
    print("check first: ", q.first())

