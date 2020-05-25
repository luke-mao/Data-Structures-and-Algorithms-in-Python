"""
use linked list to demonstrate the stack ADT
"""

class Empty(Exception): pass

# this is a node in the linked list
class Node(object):

    __slots__ = ("_element", "_next")

    def __init__(self, element, next):
        self._element = element
        self._next = next
    

# use linked list to demonstrate stack ADT
class StackUseLinkedList:

    def __init__(self):
        self._head = None
        self._size = 0
    
    def is_empty(self):
        return self._size == 0
    
    def __len__(self):
        return self._size
    
    def push(self, value):
        # add a value to the head
        new_node = Node(value, None)        # a new node
        new_node._next = self._head         # this new node is the head, so its "next" points to the old head
        self._head = new_node               # reset the head
        self._size += 1

        # can simply to 3 lines:
        # new_node = Node(value, self._head)
        # self._head = new_node
        # self._size += 1
    
    def pop(self):
        # pop the head out
        if self.is_empty():
            raise Empty("The stack is empty")
        else:
            result = self._head._element
            self._head = self._head._next
            self._size -= 1
            return result
    
    def top(self):
        if self.is_empty():
            raise Empty("The stack is empty")
        else:
            return self._head._element

    def show(self):
        """just for debug purpose"""
        if self.is_empty():
            print("Empty stack")
        else:
            print("stack top => bottom")
            node = self._head
            while node is not None:
                print(node._element, end='  ')
                node = node._next
            print()


if __name__ == '__main__':
    s = StackUseLinkedList()
    for i in range(20): s.push(i)
    s.show()

    for _ in range(5):  print(s.pop())
    s.show()
    print(len(s))

