"""
modify the textbook stack ADT,
so that its maximum capacity is "maxlen", default value is None.
"""

# define the exception for empty and full stack
class EmptyStack(Exception):    pass

class FullStack(Exception):     pass


# define the stack
class ArrayStack:

    def __init__(self, maxlen=None):
        if maxlen is None:
            raise EmptyStack("Define the max length of the stack")
        
        self._data = [None] * maxlen
        self._n = 0
        self._capacity = maxlen
    
    def is_full(self):      return self._n == self._capacity

    def is_empty(self):     return self._n == 0

    def push(self, value=None):
        if value is None:
            raise ValueError("input value for stack.push")
            
        if self.is_full():
            raise FullStack("Stack is full already")

        self._data[self._n] = value
        self._n += 1
    
    def pop(self):
        if self.is_empty():
            raise EmptyStack("Stack is empty already")
        
        value = self._data[self._n - 1] 
        self._data[self._n - 1] = None
        self._n -= 1
        return value
    
    def top(self):
        if self.is_empty():
            raise EmptyStack("Stack is empty already")

        return self._data[self._n - 1]
    

if __name__ == '__main__':
    s = ArrayStack(3)
    print(s.is_empty())
    s.push(6)
    s.push(7)
    s.push(1)

    print(s.pop())
    print(s.pop())



