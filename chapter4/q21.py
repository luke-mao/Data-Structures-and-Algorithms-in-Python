"""
given an ascending list with n elements, they are all unique.
recursion, find two elements whose sum = k, if exist
"""

def find_with_recursion(data, k):
    return recursion_func(data, k, 0, len(data)-1)


def recursion_func(data, k, left, right):
    if left >= right:
        return "None pairs match"
    else:
        sum = data[left] + data[right]
        if sum == k:    return data[left], data[right]
        elif sum > k:   return recursion_func(data, k, left, right-1)
        else:           return recursion_func(data, k, left+1, right)


def find_no_recursion(data, k):
    """no recursion, double pointer to find the value"""
    left, right = 0, len(data)-1

    while left < right:
        sum = data[left] + data[right]
        if sum == k:
            return data[left], data[right]
        elif sum > k:
            right -= 1
        elif sum < k:
            left += 1
    
    return "None pairs match"


if __name__ == '__main__':
    data = [1, 4, 6, 7, 10, 18, 20, 56, 77, 100, 150, 200, 500, 900]

    print(find_no_recursion(data, 3))
    print(find_no_recursion(data, 17))
    print(find_no_recursion(data, 97))

    print()

    print(find_with_recursion(data, 3))
    print(find_with_recursion(data, 17))
    print(find_with_recursion(data, 97))