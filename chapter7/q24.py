"""
give a complete implementation of the stack ADT,
using a singly linked list that includes a header sentinel
"""

class Empty(Exception): pass

class StackUsingSinglyLinkedList:

    class _Node:
        __slots__ = '_element', '_next'
        def __init__(self, element, next):
            self._element = element
            self._next = next

    """stack ADT"""

    def __init__(self):
        self._size = 0
        self._head = self._Node(None, None)
    
    def is_empty(self):     return self._size == 0
    def __len__(self):      return self._size

    def top(self):
        if self.is_empty():
            raise Empty("The stack is already empty")
        
        top_node = self._head._next 
        return top_node._element
    
    def push(self, value):
        # the value is pushed to the top of the stack, 
        # so need to put it in the first node

        new_node = self._Node(value, None)

        if self.is_empty():
            self._head._next = new_node
        else:
            old = self._head._next 
            self._head._next = new_node
            new_node._next = old
        
        self._size += 1
    
    def pop(self):
        # update the head
        if self.is_empty():
            raise Empty("The stack is already empty")
        
        # extract the poped_node and its value
        poped_node = self._head._next 
        value = poped_node._element 

        if self._size == 1: # only one element
            self._head._next = None
        else:   # more than 1 element
            self._head._next = poped_node._next 

        poped_node._next = None
        poped_node._element = None

        self._size -= 1
        return value
    
    def show(self): # for debug purpose
        if self.is_empty():
            print("Empty stack")
        else:
            print("stack top <= bottom")
            node = self._head._next 
            while node is not None:
                print(node._element, end='  ')
                node = node._next
            print()


if __name__ == '__main__':
    s = StackUsingSinglyLinkedList()
    for i in range(20):
        s.push(i)
    s.show()

    for _ in range(15):
        print(s.pop())
    s.show()

    print("length, ", len(s))
