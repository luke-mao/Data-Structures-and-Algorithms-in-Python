"""
change to the code q1
"""

import sys
data = []

b = sys.getsizeof(data)
print("Length: {}".format(len(data)))

for _ in range(50):
    data.append(None)
    if sys.getsizeof(data) != b:
        b = sys.getsizeof(data)
        print("Length: {}".format(len(data)))