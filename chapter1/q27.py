"""
original code to determine the factors
"""

def factors(n):
    k = 1
    while k**2 < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    
    if k ** 2 == n:
        yield k 


def factors2(n):
    k = 1
    buffer = []
    while k ** 2 < n:
        if n % k == 0:
            yield k
            buffer.append(n//k)
        
        k+= 1
    
    if k ** 2 == n:
        yield k
    
    for i in range(1, len(buffer)+1):
        yield buffer[-i]


if __name__ == '__main__':
    
    f1 = factors2(100)
    for i in f1:
        print(i)        # the result  is 1 100 2 50 4 25 5 20 10


