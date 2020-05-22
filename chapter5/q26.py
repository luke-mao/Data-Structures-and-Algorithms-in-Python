"""
a list of n elements, in the range 1 to n-1, 
there are exactly 5 same duplicate elements, 
find the duplicate
"""

def find(data):
    
    sumV = sum(data)
    arithmetic_sum = (min(data) + max(data)) * (max(data)-min(data)+1) / 2

    value = (sumV - arithmetic_sum) / 4
    return int(value)


if __name__ == '__main__':

    data1 = [1,2,2,2,2,2]
    data2 = [1,2,3,4,5,5,5,5,5,6,7,8,9,10]
    data3 = [1,2,3,4,5,6,7,8,9,10,11,11,11,11,11,12,13,14,15]

    print(find(data1))
    print(find(data2))
    print(find(data3))