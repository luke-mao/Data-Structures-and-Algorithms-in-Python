"""
compare the efficiency of list comprehension and append
"""

import time

n_list = [10**3, 10**4, 10**5]

for n in n_list:
    t1 = time.time()
    a1 = [i for i in range(n)]

    t2 = time.time()
    a2 = []
    for i in range(n):  a2.append(i)

    t3 = time.time()
    del a1, a2
    print("length={}, list comprehension = {}, append = {}, unit=10^-6 s".format(n, int((t2-t1)*10**6), int((t3-t2)*10**6)))


"""
append is slower than the list comprehension.
"""