import sys
data = []
for k in range(30):
    a = len(data)
    b = sys.getsizeof(data)
    print("length: {}, size in bytes: {}".format(a, b))
    data.append(None)