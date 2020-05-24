"""
stack, if set maxlen, 
then push an element into a full stack 
will lose one element at the bottom of the stack
"""

class Empty(Exception): pass

class ArrayStackWithLength:
    """LIFO stack, with max length, lose element during push to a full stack"""

    def __init__(self, maxlen=None):
        
        if maxlen is None:
            self._data = []
            self._fixed_length = False
        else:
            self._data = [None] * maxlen
            self._fixed_length = True
        
        self._num = 0
    
    def top(self):
        return self._data[self._num - 1]
    
    def is_empty(self):
        return self._num == 0

    def push(self, value):
        if self._fixed_length:              # if stack is full, leak one element at the bottom
            if self._num == len(self._data):
                self._data.append(value)
                self._data = self._data[1:]
            else:                           # else, simply add this element
                self._data[self._num] = value
                self._num += 1        
        else:
            self._data.append(value)
            self._num += 1


    def pop(self):
        if self.is_empty():
            raise Empty("stack is empty")
        
        if self._fixed_length:
            value = self._data[-1]
            self._data[-1] = None
            self._num -= 1
            return value
        else:
            self._num -= 1
            return self._data.pop()
    

    def show(self):
        """show the array"""
        if self.is_empty():
            print("Empty stack")
        else:
            print("bottom => top")
            string = " => ".join( str(self._data[i]) for i in range(self._num) )
            print(string)


def test_no_length_limit():
    # no length limit
    s = ArrayStackWithLength()
    print("no length limit\n")
    
    for i in range(10): s.push(i)
    print("input 10 numbers")
    s.show()

    print("\ndelete 5 numbers")
    for _ in range(5):  print(s.pop())
    s.show()

    print("top ", s.top())
    print("is empty ", s.is_empty())
    

def test_with_length_limit():
    print("with length limit 10")
    s = ArrayStackWithLength(10)
    
    print("\ninput 10 numbers")
    for i in range(10):             s.push(i)
    s.show()

    print("\nnow full, input another 10 numbers")
    for i in range(11, 20+1, 1):
        print("\ninput ", i)
        s.push(i)
        s.show()
    
    print("top value ", s.top())
    print("is empty: ", s.is_empty())


if __name__ == '__main__':
    # test_no_length_limit()
    test_with_length_limit()