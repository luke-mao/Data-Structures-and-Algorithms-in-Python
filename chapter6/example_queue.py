"""
textbook example: queue.
iterate around the array to reuse all spaces.
expand or shrink sizes if necessary
"""

class Empty(Exception):
    """error message for exception"""
    pass


class ArrayQueue:
    """FIFO queue, cyclic array"""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * self.DEFAULT_CAPACITY
        self._num = 0
        self._capacity = self.DEFAULT_CAPACITY
        self._front = 0     # the index of the first value


    def __len__(self):
        return self._num


    def is_empty(self):
        return self._num == 0


    def first(self):
        if self.is_empty():
            raise Empty("first: queue is empty")
        else:
            return self._data[self._front]


    def dequeue(self):
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


    def enqueue(self, value):
        
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

    
    def show(self):
        if self.is_empty():
            print("Empty queue")
        else:
            string = " <= ".join(str(self._data[i % self._capacity]) for i in range(self._front, self._front+self._num, 1))
            print(string)


if __name__ == '__main__':
    
    q = ArrayQueue()
    
    for i in range(30):
        q.enqueue(i)
    
    q.show()

    for _ in range(20):
        print(q.dequeue())
    q.show()

    print(len(q))
    print(q.first())
    print(q.is_empty())