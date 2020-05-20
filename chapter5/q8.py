import time

print("Length   pop(0)   pop(n//2)  pop()")

for i in [10**3, 10**4, 10**5, 10**6, 10**7, 10**8]:
    data = [1]*i
    t1 = time.time()
    data.pop(0)
    t2 = time.time()
    data.pop(i//2)
    t3 = time.time()
    data.pop()
    t4 = time.time()

    print("{}, 0=>{:6f}, mid=>{:6f}, last={:6f}".format(i, (t2-t1)*10**6, (t3-t2)*10**6, (t4-t3)*10**6))

"""
cost: pop(0) > pop(mid) > pop(final),
the overall amortization is around O(n).
same as insert.
"""