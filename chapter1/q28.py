"""
calculate the p-norm of a vector v in list
"""
import math

def norm(v, p):
    if not isinstance(p, int):
        raise ValueError("p should be a positive integer")
    if not p >= 1:
        raise ValueError("p should >= 1")

    result = sum([i**p for i in v])
    return result ** (1.0 / p)


if __name__ == '__main__':
    v = [3, 4, 5]
    p = 2
    print(norm(v, p))
