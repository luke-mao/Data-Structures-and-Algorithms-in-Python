"""
only use addition and subtraction, 
write a recursion calculate m * n,
givne: m, n are positive integers
"""

def product(m, n):
    if n == 1:
        return m
    else:
        return m + product(m, n-1)


if __name__ == '__main__':
    print("{}, {}".format(product(50, 70), 50*70))
    print("{}, {}".format(product(45, 15), 45*15))