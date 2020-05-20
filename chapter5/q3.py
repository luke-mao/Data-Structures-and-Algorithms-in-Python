"""
prove that when a value is poped, the list size will sometimes shrink
"""

import sys
data = [None] * 100

for _ in range(100):
    print("Length {}, Size in bytes {}".format(len(data), sys.getsizeof(data)))
    data.pop()


"""
The result is similar, size decrease as a multiple of 8 bytes
"""