"""
implement a function that counts the number of nodes
in a circularly linked list
"""

from example_circular_linked_list import CircularLinkedList

def length(current):
    # given a node of a circular linked list, find the length
    node = current
    num = 1

    node = node._next   # move to next node

    while node != current:
        num += 1
        node = node._next

    return num


if  __name__ == '__main__':
    q = CircularLinkedList()
    for i in range(50):     q.add(i)
    q.show()

    # give several starting node of the queue, find the length
    q1 = q._tail
    for _ in range(10):     q1 = q1._next
    print("length ", length(q1))

    q2 = q._tail
    for _ in range(30):     q2 = q2._next
    print("length ", length(q2))

    q3 = q._tail
    for _ in range(40):     q2 = q2._next
    print("length ", length(q3))

    q4 = q._tail
    print("length ", length(q4))
