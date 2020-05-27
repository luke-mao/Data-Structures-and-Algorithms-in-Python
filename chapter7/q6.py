"""
suppose that x and y are references to nodes of circularly linked lists,
although not necessarily the same list. 
describe a fast algorithm for telling if x and y belong to the same list.

method:
    scan one of the list, and compare
"""
from example_circular_linked_list import Node
from example_circular_linked_list import CircularLinkedList

def check(node1:Node, node2:Node):
    # return True if they are the same list, false if not
    if node1 == node2:
        return True
    else:
        a = node1._next
        flag = False

        while True:
            if a == node2:
                flag = True
                break            
            if a == node1:
                break

            a = a._next
        
        return flag


if __name__ == '__main__':

    q1 = CircularLinkedList()
    for i in range(20):
        q1.add(i)
    q1.show()

    q2 = CircularLinkedList()
    for i in range(30, 40):
        q2.add(i)
    q2.show()

    print(check(q1._tail, q2._tail))

    print(check(q1._tail, q1._tail._next._next._next))


