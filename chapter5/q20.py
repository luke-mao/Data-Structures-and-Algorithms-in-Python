"""
test 4 different methods to construct a long string
"""

import time

def method1(n):
    letters = ""
    for _ in range(n):
        letters += "a"
    return letters


def method2(n):
    temp = []
    for _ in range(n):
        temp.append("a")
    
    return "".join(temp)


def method3(n):
    return "".join(["a" for _ in range(n)])


def method4(n):
    return "".join("a" for _ in range(n))


if __name__ == '__main__':
    n_list = [10**4, 10**5, 10**6, 10**7]
    m1 = [None] * len(n_list)
    m2 = [None] * len(n_list)
    m3 = [None] * len(n_list)
    m4 = [None] * len(n_list)

    for i in range(len(n_list)):
        a = time.time()
        result = method1(n_list[i])
        b = time.time()
        del result
        m1[i] = int((b-a)*10**6)
    
    for i in range(len(n_list)):
        a = time.time()
        result = method2(n_list[i])
        b = time.time()
        del result
        m2[i] = int((b-a)*10**6)

    for i in range(len(n_list)):
        a = time.time()
        result = method3(n_list[i])
        b = time.time()
        del result
        m3[i] = int((b-a)*10**6)

    for i in range(len(n_list)):
        a = time.time()
        result = method4(n_list[i])
        b = time.time()
        del result
        m4[i] = int((b-a)*10**6)
    
    print(m1)
    print(m2)
    print(m3)
    print(m4)


"""
the string append method is difinitely worse than the others.
for the others, the time does not varies a lot, seems to finish all in O(n)
"""