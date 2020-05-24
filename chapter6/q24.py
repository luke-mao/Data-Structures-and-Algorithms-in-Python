"""
use a Queue to realize Stack ADT.
only minor changes to the code from example_queue.py 

time:
pop: O(n): need to rotate the queue
push: O(1)
top: O(1)
"""

# empty exception
class Empty(Exception):
    pass


class ArrayStackUsingQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * self.DEFAULT_CAPACITY
        self._num = 0
        self._capacity = self.DEFAULT_CAPACITY
        self._front = 0     # the index of the first value


    def is_empty(self):
        return self._num == 0

    def top(self):
        return self._data[(self._front + self._num - 1) % self._capacity]

    def push(self, value):
        """time O(1), unless expand the size"""
        self._enqueue(value)

    def pop(self):
        """
        time O(n), need to rotate the whole queue.
        total self._num  elements, so enqueue(dequeue) self._num-1 times,
        then the last dequeue returns the value        
        """

        for _ in range(self._num - 1):
            self._enqueue(self._dequeue())
        
        return self._dequeue()


    # original code from ArrayQueue, used in "push"
    def _enqueue(self, value):
        
        # if already full, then double the size
        if self._num == self._capacity:
            new_data = [None] * (self._capacity * 2)
            
            # copy everything
            for i in range(self._num):
                new_data[i] = self._data[(self._front+i) % self._capacity]
            
            self._data = new_data[:]
            self._capacity *= 2
            self._front = 0


        index = (self._front + self._num) % self._capacity
        self._data[index] = value
        self._num += 1


    def _dequeue(self):
        if self.is_empty():
            raise Empty("dequeue: queue is empty")
        
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1) % self._capacity
        self._num -= 1

        # if the total number stored is less than 0.25*capacity, shrink half of the size
        if self._capacity > self.DEFAULT_CAPACITY and self._num <= self._capacity // 4:
            new_data = [None] * max(self._capacity // 2, self.DEFAULT_CAPACITY) # minimum capacity = 10
            for i in range(self._num):
                new_data[i] = self._data[(self._front + i) % self._capacity]
            
            self._data = new_data[:]
            self._capacity = self._capacity // 2
            self._front = 0
            # self._num does not change, already minus 1 at above        
            
        return value
    

    def show(self):
        if self.is_empty():
            print("Empty Stack")
        else:
            # minor change of code from ArrayQueue
            string = " <= ".join(str(self._data[(self._front + i) % self._capacity]) for i in range(self._num-1, -1, -1) )
            print(string)


if __name__ == '__main__':
    s = ArrayStackUsingQueue()

    for i in range(30):     s.push(i)
    s.show()

    for _ in range(25):     print(s.pop())
    s.show()
    print(s.top())

    for _ in range(5):      print(s.pop())
    print(s.is_empty())
