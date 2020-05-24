"""
modify ArrayQueue, so that the user can input a variable "maxlen", default value is None.
if the user choose to set it, then the enqueue can trigger QueueFull exception.
"""

from example_queue import ArrayQueue
from example_queue import Empty

class Full(Exception):         pass

class ArrayQueueWithLengthLimit(ArrayQueue):

    def __init__(self, maxlen=None):
        # note the way to inherit the __init__
        # no need to put self!!! not __init__(self) !!!
        super().__init__()

        if maxlen is not None:
            self._data = [None] * maxlen
            self._capacity = maxlen
            self._fixed_length = True
        else:
            self._fixed_length = False
    

    """len, first, is_empty are all the same as ArrayQueue"""

    def dequeue(self):
        """if length not fixed, same as before. if fixed, then do not shrink size"""
        if not self._fixed_length:
            return super().dequeue()    # no need to do super().dequeue(self) !!!!, no self !!!
        else:
            # if the length is fixed, then 
            if self.is_empty():
                raise Empty("dequeue: queue is empty")
        
            value = self._data[self._front]
            self._data[self._front] = None
            self._front = (self._front+1) % self._capacity
            self._num -= 1

            return value
    
    def enqueue(self, value):
        
        if not self._fixed_length:
            super().enqueue(value)
        else:
            if self._num == self._capacity:
                raise Full("Queue is full already")
            else:
                super().enqueue(value)
    

if __name__ == '__main__':
    q = ArrayQueueWithLengthLimit(10)
    for i in range(10):
        q.enqueue(i)

    q.show()    
    print("length: {}".format(len(q)))

    # q.enqueue(12)  # reach max size, will cause exception

    for _ in range(8):  print(q.dequeue())
    q.show()
    print("length: {}".format(len(q)))
    print("first: {}".format(q.first()))

        