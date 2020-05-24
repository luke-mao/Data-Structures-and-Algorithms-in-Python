"""
textbook example: double ended queue.
use cyclic array structure, change size if necessary.
"""

class Empty(Exception):
    pass


class ArrayDoubleEndedQueue:
    """double-ended-queue, both ends can add or delete"""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * self.DEFAULT_CAPACITY
        self._front = 0
        self._capacity = self.DEFAULT_CAPACITY
        self._num = 0


    def add_first(self, value):
        
        if self._num == self._capacity:
            # resize to double the capacity
            new = [None] * (self._capacity * 2)
            
            for i in range(self._num):
                # note, use i+1, since you are going to add one at the front
                new[i+1] = self._data[(self._front+i) % self._capacity]
            
            self._data = new[:]
            self._front = 1         # currently the first value starts at [1]
            self._capacity *= 2
        
        
        self._front = (self._front - 1) % self._capacity
        self._data[self._front] = value    
        self._num += 1 


    def add_last(self, value):
        # similar code to the add_first

        if self._num == self._capacity:
            # resize to double the capacity
            new = [None] * (self._capacity * 2)
            
            for i in range(self._num):
                # note, use i, since the new data is appended to the last
                new[i] = self._data[(self._front+i) % self._capacity]
            
            self._data = new[:]
            self._front = 0         # front set to 0, unlike add_first
            self._capacity *= 2
        
        # note the difference to the add_first
        self._data[(self._front + self._num) % self._capacity] = value   
        self._num += 1  


    def delete_first(self):
        if self._num == 0:
            raise Empty("double-ended-queue is already empty")

        value = self._data[self._front] # after potential resizing, return this value

        self._data[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._num -= 1

        if self._capacity > self.DEFAULT_CAPACITY and self._num <= self._capacity // 4:
            self._down_size()

        return value


    def delete_last(self):
        # delete the last value

        if self._num == 0:
            raise Empty("double-ended-queue is already empty")

        if self._num == 0:
            raise Empty("double-ended-queue is already empty")
        
        value = self._data[(self._front + self._num - 1) % self._capacity] # after potential resizing, return this value

        self._data[(self._front + self._num - 1) % self._capacity] = None
        self._num -= 1

        if self._capacity > self.DEFAULT_CAPACITY and self._num <= self._capacity // 4:
            self._down_size()

        return value


    def first(self):
        if self._num == 0:
            raise Empty("double-ended-queue is already empty")
        return self._data[self._front]

    def last(self):
        if self._num == 0:
            raise Empty("double-ended-queue is already empty")        
        # !!! minus 1
        return self._data[(self._front + self._num - 1) % self._capacity]

    def is_empty(self):
        return self._num == 0

    def __len__(self):
        return self._num

    def show(self):
        string = " <= ".join(str(self._data[i % self._capacity]) for i in range(self._front, self._front+self._num, 1))
        print(string)

    # additional function for downsize
    # upsize is a little different for add_first and add_last, so does not combine to one
    def _down_size(self):
        # downsize operation for delete_first and delete_last
        new_data = [None] * max(self._capacity // 2, self.DEFAULT_CAPACITY) # default capacity = 10
        for i in range(self._num):
            new_data[i] = self._data[(self._front + i) % self._capacity]
        
        self._data = new_data[:]
        self._capacity = self._capacity // 2
        self._front = 0


if __name__ == '__main__':
    q = ArrayDoubleEndedQueue()

    for i in range(30):
        if i % 2 == 0:
            q.add_first(i)
        else:
            q.add_last(i)

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