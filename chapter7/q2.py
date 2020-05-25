"""
a good algorithm for concatenating two singly linked list together,
given both the head node of each list
"""

from example_singly_linked_list import SinglyLinkedList

def concat(L, M):
    # concat two linked lists together
    # the result is stored in L
    if M._head is not None:         # if M is none, does not matter what L is, simply return L
        
        if L._head is None:         # if L._head is None, copy M
            L._head = M._head
            L._size = M._size
        else:
            head = L._head
            while head._next is not None:
                head = head._next
            head._next = M._head

    # if M._head is None, don't need to do anything


if __name__ == '__main__':
    L = SinglyLinkedList()
    for i in range(10):     L.add(i)
    print("L:")
    L.show()

    M1 = SinglyLinkedList()
    for j in range(5):  M1.add(j)
    print("M1: ")
    M1.show()

    # normal concat, two not None linked list
    concat(L, M1)
    L.show()        # L changed, since it stores the result
    print()

    # M is None, concat
    M2 = SinglyLinkedList()
    M2.show()
    concat(L, M2)
    L.show()        # L remain unchanged
    print()

    # L is None, M is not None
    L2 = SinglyLinkedList()
    L2.show()
    concat(L2, M1)
    L2.show()