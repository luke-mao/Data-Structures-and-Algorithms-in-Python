"""
find the second-to-last node in a singly linked list.
the last node is indicated by a "next" reference of None.

Use two pointers: this idea is quite common in Leetcode
"""

from example_singly_linked_list import SinglyLinkedList

def find(linked_list):
    # import a linked list, find the second-to-last node, print the value
    # if the list is purely None, return None
    # if the list only 1 element, return None
    # for other: return the second-to-last node
    
    if linked_list._head is None:
        return None
    elif linked_list._head._next is None:
        return None
    else:
        prev = linked_list._head
        current = prev._next

        while current is not None:
            prev = prev._next 
            current = current._next
        
        return prev


if __name__ == '__main__':
    
    q = SinglyLinkedList()
    for i in range(20):
        q.add(i)
    q.show()

    print(find(q)._element)

    q2 = SinglyLinkedList()
    q2.show()
    if find(q2) is None:
        print("None")
    else:
        print(find(q2))

    q3 = SinglyLinkedList()
    q3.add(3)
    q3.show()
    if find(q2) is None:
        print("None")
    else:
        print(find(q2))
