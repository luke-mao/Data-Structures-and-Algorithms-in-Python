"""
swap two nodes in a singly linked list,
not just swap the contents, but two nodes completely.
swap: given the reference only to the two nodes and the head.

method:
    consider all four scenarios. 
    quite difficult to do in the singly-linked list.
    for double-linked-list, since there are the dummy head and trailer, everything will be easier.
"""

from example_singly_linked_list import SinglyLinkedList
from example_singly_linked_list import _Node

def swap(head:_Node, node1:_Node, node2:_Node):
    """
    Assume node1 is before node2 !!!
    Consider the following four scenario:
        1. two nodes are equal => do nothing
        2. node1 is the head => consider if two nodes are next to each other, 
           or are originally separated
        3. node1 is not the head, consider if two nodes are next to each other
        4. node1 is not the head, consider two nodes are separated originally    
    """

    if node1 == node2:
        pass

    elif node1 == head:
        # if the two nodes are not closely linked
        if node1._next != node2:
            after1 = node1._next
            
            # find the predecessor of node2
            after2 = node2._next
            prev2 = head
            while prev2._next != node2:    prev2 = prev2._next

            # relink the list
            node2._next = after1
            head = node2
            prev2._next = node1
            node1._next = after2
        
        else:   # if the two nodes are closely linked
            after2 = node2._next
            # relink the list: sequence = head/node2, node1, after2
            head = node2
            head._next = node1
            node1._next = after2
    
    elif node1._next == node2:        # node1 is assumed to be before node2
        # find the predecessor before node1
        before1 = head
        while before1._next != node1:   before1 = before1._next
        # find the after node2
        after2 = node2._next

        # relink the list
        before1._next = node2
        node2._next = node1
        node1._next = after2 
    
    else:
        # this is the most general situation: no node is the head, and two nodes are separated
        # node1 != head and node2 != head and node1._next != node2 and node2._next != node1
        # find the predecessor of node1 and node2
        after1 = node1._next
        prev1 = head
        while prev1._next != node1:    prev1 = prev1._next
        
        after2 = node2._next
        prev2 = head
        while prev2._next != node2:    prev2 = prev2._next

        # now find the previous and after nodes for both node1 and node2
        # relink the list
        prev1._next = node2
        node2._next = after1

        prev2._next = node1
        node1._next = after2

    return head

def test_swap(list1, num1, num2):
    # choose two nodes and swap
    node1 = list1._head
    for _ in range(num1):  node1 = node1._next
    node2 = list1._head
    for _ in range(num2): node2 = node2._next
    
    # the swap functions takes the head and two nodes
    # for simplicity, we assume node1 is before node2
    # return the original/new head.
    # new head is assigned if node1 is the head, i.e. need to swap the head with another element
    print("swap the two node: {} and {}".format(node1._element, node2._element))
    list1._head = swap(list1._head, node1, node2)     
    list1.show()
    print()


if __name__ =='__main__':

    list1 = SinglyLinkedList()
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
