"""
initialize with a non-zero length, 
try: start with various initial size, but all fill with "None"
"""

import sys

# function to record the update in size
def test(length):
    print("{}".format("-"*20))
    print("Initial length = {}".format(length))
    data = [None] * length
    change = []

    old_size = sys.getsizeof(data)
    for i in range(5000):
        if sys.getsizeof(data) != old_size:
            change.append(len(data))
            old_size = sys.getsizeof(data)
        
        data.append(None)
    
    print("Change size at = {}".format(str(change)))


if __name__ == '__main__':

    initial_length_list = [1, 10, 100, 1000]
    for initial_length in initial_length_list:
        test(initial_length)


"""
The increment method is not simply doubling the size. 
If look at the actual size change, all follows 64 bit address. 
"""