"""
use stack to printout all combination of elements in a list
"""

from example_stack import ArrayStack

def _recursion_no_stack(s, data):
    if len(data) == 0:
        print(s)
    else:
        for i in range(len(data)):
            s2 = s + [data[i]]
            data2 = data[:]
            data2.pop(i)
            _recursion_no_stack(s2, data2)


def recursion_no_stack(data):
    _recursion_no_stack([], data)



def no_recursion_use_stack(data):
    """use stack and without recursion, is quite similar to the code using recursion"""
    s = ArrayStack()

    for each in data:
        s.push( ([each], set(data)-set([each])   ) )
    
    while not s.is_empty():
        formed_list, remaining_item_set = s.pop()
        if len(remaining_item_set) == 0:
            print(formed_list)
        else:
            for each in remaining_item_set:
                formed_list_copy = formed_list[:]
                formed_list_copy.append(each)
                s.push( (formed_list_copy, remaining_item_set - set([each]) ) )


if __name__ == '__main__':
    recursion_no_stack([1,2,3,4])
    # no_recursion_use_stack([1,2,3,4])