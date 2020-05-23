"""
recursion, all subsets of a set with n elements.
note: just the subset, not combination of elements
"""


def subset(data):
    """
    return the subset, in numerical order.
    method:
        subset number = 2^n = 2*2^(n-1).....
        so take one element out, then calculate the subsets of the remaining, 
        then append the element to everything, and also append the element itself
    """
    if data == []:
        return [[]]
    else:
        subsets_of_remaining  = subset(data[:-1])

        return sorted(subsets_of_remaining + [[data[-1]]+ each for each in subsets_of_remaining])


if __name__ == '__main__':
    data = [1,2,3]
    print(subset(data))
    print()


    data2 = [1,2,3,4]
    print(subset(data2))
    print()



