"""
given a list with n digits, from 1 to n-1, only one number is duplicated.
find the number.
method: using sum (much quicker than the textbook solution)
"""

def find_duplicate(data):
    data_sum = sum(data)
    minV, maxV = min(data), max(data)
    sequence_sum = (minV + maxV) * (len(data)-1) / 2
    return data_sum - sequence_sum 


if __name__ == '__main__':
    
    data = [1, 2, 3, 3]
    data2 = [1, 2, 3, 4, 5, 5, 6]
    data3 = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]

    print(find_duplicate(data))
    print(find_duplicate(data2))
    print(find_duplicate(data3))