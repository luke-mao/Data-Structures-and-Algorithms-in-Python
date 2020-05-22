"""
textbook example of Stack:
inifinite stack
"""

class Empty(Exception):
    """error message for empty stack operation"""
    pass


class ArrayStack:
    """LIFO stack implementation"""

    def __init__(self):
        self._data = []
    
    def  __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, value):
        self._data.append(value)
    
    def top(self):
        """return the last element in the list, but does not remove it"""
        if self.is_empty(): # if the stack is empty
            raise Empty("stack is empty")
        else:
            return self._data[-1]
    
    def pop(self):
        """return and remove the last element in the list"""
        if self.is_empty():
            raise Empty("stack is empty")
        else:
            return self._data.pop()
    
    def show(self):
        """show the array"""
        if self.is_empty():
            print("Empty stack")
        else:
            print("bottom=>top")
            print(" => ".join(str(i) for i in self._data))


if __name__ == '__main__':

    a = ArrayStack()
    print(len(a))
    a.push(5)
    a.push(6)
    print(a.top())
    print(a.pop())
    print(len(a))
    print(a.pop())
    # print(a.pop())
        