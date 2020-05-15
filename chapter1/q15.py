"""
given an integer data, determine if all numbers are different,
i.e. all numbers are unique

note:
xor: two values are equal, result = 0, otherwise result = 1
xor can be used to find one unique number, but cannot check if all numbers are unique
"""

def check_unique1(data):
    return len(data) == len(set(data))

def check_unique2(data):
    data2 = sorted(data)                # sort data, around O(N*log(N))， sort is on the original list, sorted return a new list
    for i in range(0, len(data2)-1):    # O(N)
        if data2[i] ^ data2[i+1] == 0:
            return False
    return True



if __name__ == '__main__':
    data1 = [1,3,5,7,9,1]
    data2 = [2,5,0,9]

    print("{}:{}".format(check_unique1(data1), data1))
    print("{}:{}".format(check_unique1(data2), data2))

    print("{}:{}".format(check_unique2(data1), data1))
    print("{}:{}".format(check_unique2(data2), data2))