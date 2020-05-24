"""
use an empty queue Q to scan a stack S with n elements.
scan to find the true index of an element in the stack.
need to do the iteration twice, since the original stack should not be modified
"""

from example_stack import ArrayStack
from example_queue import ArrayQueue

def find(s, target):
    """
    import the stack, find the index of the target.
    return the index in two ways, count from top and count from bottom.
    note: index start from 0
    """

    q = ArrayQueue()
    while not s.is_empty():
        q.enqueue(s.pop())
    
    num = len(q)

    index = 0
    find = False
    while not q.is_empty():
        if (not find) and (q.first() == target):
            find = True
        
        if not find:
            index += 1

        s.push(q.dequeue())
    
    # does not matter find or not find, need to return s in the original state
    while not s.is_empty():
        q.enqueue(s.pop())
    while not q.is_empty():
        s.push(q.dequeue())
    
    if find:
        return index, num-index-1
    else:
        raise ValueError("target {} not in the stack".format(target))



if __name__ == '__main__':
    s = ArrayStack()
    values = [2,5,7,9,10,4,1,0]
    for value in values:     s.push(value)
    s.show()

    for value in [2, 7, 4]:
        i1, i2 = find(s, value)
        print("count from top index = {}, from bottom index = {}".format(i1, i2))