"""
compare the efficiency of list.extend and list.append
"""

import time

def use_extend(data, other):
    return data.extend(other)

def use_append(data, other):
    for each in other:
        data.extend(other)
    return data


if __name__ == '__main__':

    length_list = [10**2, 10**3, 10**4]

    for length in length_list:
        data = [None]*length
        other = [None]*length
        a = time.time()
        result1 = use_extend(data, other)
        b = time.time()
        result2 = use_append(data, other)
        c = time.time()

        print("length {}+{}: extend={}, append={}".format( length, length, int((b-a)*10**6), int((c-b)*10**6) ))

"""
extend is definitely a lot quicker than append !!!
the reason is that, "extend" sets the resulting length once for all, but during "append", the length increases slowly. 
"""
