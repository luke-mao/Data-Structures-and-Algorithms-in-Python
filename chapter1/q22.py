"""
input two same length integer list, 
return the dot product list
"""

def dot_product_list(a, b):
    if len(a) != len(b):
        raise ValueError("inputs must be same length")
    if (len(a) == 0):
        raise ValueError("input length must not equal to 0")

    c = a[:]
    for i in range(len(c)):
        c[i] *= b[i]

    return c


if __name__ == '__main__':
    a = [3,5,7]
    # b = [4,6]
    # print(dot_product_list(a, b))

    b = [4,6,8]
    print(dot_product_list(a, b))