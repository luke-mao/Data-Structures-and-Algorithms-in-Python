"""
accept a list of integer data,
determine if there is a pair of product is odd, and the two numbers are different

note: only odd * odd = odd number
"""

def find_pair(data):
    # this is my solution, use double loop, but too tedious
    for i in data[:-1]:
        if (i & 1 == 1):
            for j in data[1:]:
                if (j & 1 == 1) and (i != j):
                    return True

    return False


def find_pair2(data):
    # the textbook has a much simplier solution: simply find >= 2 odd numbers in the list is enough
    count = 0
    for i in data:
        if (i & 1 == 1):
            count += 1      # python does not support count++
            if count >= 2:
                return True
    return False



if __name__ == "__main__":
    data1 = [2,4,6,9]
    data2 = [1,2,7,4,8]

    print("{}:{}".format(find_pair(data1), data1))
    print("{}:{}".format(find_pair(data2), data2))
    
    print("{}:{}".format(find_pair2(data1), data1))
    print("{}:{}".format(find_pair2(data2), data2))
