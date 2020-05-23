"""
use a stack and queue to display all subsets of a set with n elements
"""

from example_stack import ArrayStack
from example_queue import ArrayQueue

def subset_no_recursion_use_array_queue(data):
    """
    stack to store elements yet to generate subsets,
    queue store the subsets generated so far.

    method: quite similar to the recursion method, 
            so the queue dequeue everything and append the same, and the one with new element
    """

    s = ArrayStack()
    q = ArrayQueue()

    for each in data:   s.push([each])

    while not s.is_empty():
        new = s.pop()
        q.enqueue(new)
        while q.first() != new:
            out = q.dequeue()
            q.enqueue(out)
            q.enqueue(out+new)
    
    q.enqueue([])       # manually input the empty set

    q.show()        # or can combine and return as a long list


def subset_with_recursion(data):
    if data == []:
        return [[]]
    else:
        subsets_of_remaining = subset_with_recursion(data[:-1])
        add_the_last_value = [each + [data[-1]] for each in subsets_of_remaining ]
        return sorted(subsets_of_remaining + add_the_last_value)


if __name__ == '__main__':
    # result = subset_with_recursion([1,2,3])
    # for each in result:     print(each)

    subset_no_recursion_use_array_queue([1,2,3])