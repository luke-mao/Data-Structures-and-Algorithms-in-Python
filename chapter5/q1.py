"""
code test using 5.1
"""

import sys
data = []

for k in range(26):
    a = len(data)
    b = sys.getsizeof(data)
    print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))
    data.append(None)

"""
Length:   0; Size in bytes:   56
Length:   1; Size in bytes:   88
Length:   2; Size in bytes:   88
Length:   3; Size in bytes:   88
Length:   4; Size in bytes:   88
Length:   5; Size in bytes:  120
Length:   6; Size in bytes:  120
....

Similar answers to the book, except the starting size is smaller than the result on the book.
The increment is every 32 bytes => 64 bit address

"""