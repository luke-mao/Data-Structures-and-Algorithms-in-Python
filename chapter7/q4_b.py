"""
for doubly linked list, swap two elements.
much easier than the singly linked list in q4_a.py .

the test functions prints both the _prev and _next sequence,
in order to check the correctness of the link in both directions
"""

from example_doubly_linked_list_simple import SimpleDoublyLinkedList

def swap(node1, node2):
    # for doubly linked list, since there are dummy head and trailers,
    # do not need input list._head

    if node1 == node2:
        pass
    
    elif node1._next == node2:
        prev1 = node1._prev
        after2 = node2._next

        # relink the next
        prev1._next = node2
        node2._next = node1
        node1._next = after2

        # relink the prev
        after2._prev = node1
        node1._prev = node2
        node2._prev = prev1
    
    else:
        prev1, after1 = node1._prev, node1._next
        prev2, after2 = node2._prev, node2._next

        # relink the next
        prev1._next = node2
        node2._next = after1

        prev2._next = node1
        node1._next = after2

        # relink the prev
        after2._prev = node1
        node1._prev = prev2

        after1._prev = node2
        node2._prev = prev1

    # no need to return the list head, since it is a dummy head


def test_swap(list1, num1, num2):
    # choose two nodes and swap, num1 and num2 both +1 to comply with the dummy head
    node1 = list1._head
    for _ in range(num1+1):  node1 = node1._next
    node2 = list1._head
    for _ in range(num2+1): node2 = node2._next
    
    # the swap functions takes only the two nodes
    # for simplicity, we assume node1 is before node2
    # does not return anything
    print("swap the two node: {} and {}".format(node1._element, node2._element))
    swap(node1, node2)     
    list1.show()
    print()


if __name__ =='__main__':
    list1 = SimpleDoublyLinkedList()
    for i in range(20):     list1.add(i)
    print("original:")
    list1.show()
    print()

    # swap middle two nodes, and also test the boundary
    test_swap(list1, 3, 5)      # two middle index
    test_swap(list1, 10, 18)    # two middle index
    test_swap(list1, 12, 19)    # one middle + one tail
    test_swap(list1, 5, 6)      # two nodes next to each other
    test_swap(list1, 0, 1)      # swap head and the next one
    test_swap(list1, 0, 7)      # swap head and a middle node
    test_swap(list1, 0, 19)     # swap the head and tail