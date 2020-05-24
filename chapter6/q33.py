"""
double ended queue ADT, include variable "maxlen", default value = None.
if maxlen is set, either add_first or add_last will result in the loss of one element at the opposite direction
"""

from example_double_ended_queue import ArrayDoubleEndedQueue
from example_double_ended_queue import Empty

class Full(Exception):  pass

class ArrayDoubleEndedQueue2(ArrayDoubleEndedQueue):
    """if maxlen is set, insert one value will lose the value at the opposite end"""

    def __init__(self, maxlen=None):
        
        if maxlen is None:
            super().__init__()
            self._fixed_length = False
        
        else:
            self._fixed_length = True
            self._data = [None] * maxlen
            self._front = 0
            self._capacity = maxlen
            self._num = 0
    
    def add_last(self, value):
        # slightly modify the original code
        if self._fixed_length:
            if self._num == self._capacity:
                # add last, lose one value from the first
                super().delete_first()
                
            super().add_last(value)
        
        else:
            super().add_last(value)
    
    def add_first(self, value):
        # slightly modify the original code
        if self._fixed_length:
            if self._num == self._capacity:
                # add first to a full queue, lose one value from the last end
                super().delete_last()
            
            super().add_first(value)

        else:
            super().add_first(value)

    def delete_first(self):
        
        if self._fixed_length:
            # delete, but do not shrink the size
            if self._num == 0:
                raise Empty("double-ended-queue is already empty")

            value = self._data[self._front] # after potential resizing, return this value

            self._data[self._front] = None
            self._front = (self._front + 1) % self._capacity
            self._num -= 1
            return value

        else:
            return super().delete_first()
    
    def delete_last(self):
        if self._fixed_length:
            if self._num == 0:
                raise Empty("double-ended-queue is already empty")
        
            value = self._data[(self._front + self._num - 1) % self._capacity] # after potential resizing, return this value

            self._data[(self._front + self._num - 1) % self._capacity] = None
            self._num -= 1
            return value
        
        else:
            return super().delete_last()

    def first(self):    return super().first()
    def last(self):     return super().last()
    def is_empty(self): return super().is_empty()
    def __len__(self):  return super().__len__()
    def show(self):     super().show()


def test_no_length_limit():
    q = ArrayDoubleEndedQueue2()

    for i in range(30):
        if i % 2 == 0:  q.add_first(i)
        else:           q.add_last(i)

    print("initial: insert 30 numbers")
    q.show()

    for _ in range(10):
        print(q.delete_first())
        print(q.delete_last())
    
    print("delete first 10 and last 10")
    q.show()
    print("length {}".format(len(q)))

    print("first value: {}".format(q.first()))
    print("last value: {}".format(q.last()))
    print("is empty: {}".format(q.is_empty()))


def test_with_length_limit():
    
    print("length limit 30")
    q = ArrayDoubleEndedQueue2(20)

    for i in range(20):
        if i % 2 == 0:  q.add_first(i)
        else:           q.add_last(i)
    q.show()
    print("length {}".format(len(q)))

    print("\ninsert 5 values to the last")
    for i in range(21, 25+1, 1):
        q.add_last(i)
        print("insert ", i)
        q.show()
    print("length {}".format(len(q)))

    print("\ninsert 5 values to the first")
    for i in range(26, 30+1, 1):
        q.add_first(i)
        print("insert ", i)
        q.show()
    print("length {}".format(len(q)))

    print("\ndelete first 5 and last 5")
    for _ in range(5):
        print(q.delete_first())
        print(q.delete_last())
    q.show()
    print("length {}".format(len(q)))

    print("\nfirst value: {}".format(q.first()))
    print("last value: {}".format(q.last()))
    print("is empty: {}".format(q.is_empty()))
    

if __name__ == '__main__':
    # test_no_length_limit()
    test_with_length_limit()