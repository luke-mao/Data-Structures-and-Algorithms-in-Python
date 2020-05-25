"""
Doubly linked list, private instance.
For each node, there are two pointers _prev and _next.
The list supports O(1) to insert and delete nodes at any position among the list.
Use dummy head and trailer to simplify the problem
"""

class Empty(Exception): pass

class _Node:
    __slots__ = '_element', '_prev', '_next'
    
    def __init__(self, element, prev, next):
        self._element = element
        self._prev = prev
        self._next = next

class _DoublyLinkedList:
    """a doubly linked list representation"""

    def __init__(self):
        self._head = _Node(None, None, None)
        self._trailer = _Node(None, None, None)
        self._size = 0

        # double direction, link two pointers
        self._head._next = self._trailer
        self._trailer._prev = self._head
    
    def __len__(self):  return self._size
    def is_empty(self): return self._size == 0

    def _insert_between(self, value, predecessor, successor):
        """insert "value" node in between predecessor and successor"""
        new_node = _Node(value, predecessor, successor)
        
        predecessor._next = new_node
        successor._prev = new_node

        self._size += 1
        return new_node     # the textbook here return the node, but actually not necessary
    
    def _delete_node(self, node):
        """delete the node"""
        predecessor = node._prev
        successor = node._next 

        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1

        
        element = node._element
        # depreciate the node for garbage recycle
        node._prev = None
        node._next = None
        node._element = None

        return element
