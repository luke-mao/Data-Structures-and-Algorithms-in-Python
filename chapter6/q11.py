"""
use collection.deque to function queue ADT
"""

import collections

class ArrayQueue(collections.deque):

    def __init__(self):
        self._q = collections.deque()
        self._num = 0
    
    def enqueue(self, value):
        self._q.append(value)
        self._num += 1
    
    def dequeue(self):
        value = self._q.popleft()
        self._num -= 1
        return value
    
    def first(self):
        return self._q[0]
    
    def is_empty(self):
        return self._num == 0
    
    def __len__(self):
        return self._num


if __name__ == '__main__':
    
    q = ArrayQueue()
    for i in range(10):     q.enqueue(i)
    print("length", len(q))
    print("first", q.first())

    print("dequeue 5 elements")
    for _ in range(8):      print(q.dequeue())
    print("length", len(q))
    print("first", q.first())
    print("is empty", q.is_empty())
