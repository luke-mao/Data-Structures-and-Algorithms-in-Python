"""
link hopping, find the middle of a doubly linked list with head and trailer setinels.
for even number: report the node slightly left of center
"""

from example_doubly_linked_list_simple import SimpleDoublyLinkedList
from example_doubly_linked_list_simple import Node

class Empty(Exception): pass

def middle(linked_list : SimpleDoublyLinkedList):
    # use the head and tail
    # fast and slow two pointers
    # fast move 2 nodes at a time, slow moves one node

    head = linked_list._head
    trailer = linked_list._trailer

    if head._next == trailer:
        raise Empty("The queue is empty")

    fast = head._next
    slow = head._next

    while True:
        if fast._next == trailer or fast._next._next == trailer:
            break
        else:
            fast = fast._next._next
            slow = slow._next

    return slow


if __name__ == '__main__':

    
    for i in range(1, 20+1):
        q = SimpleDoublyLinkedList()
        for j in range(i):
            q.add(j)

        print("original queue")
        q.show()
        print("find middle element: ", middle(q)._element)
        print()

