"""
given an unordered integer list, and an integer k.
k can be in the list, or not.
recursion, sort the list, so that elements <=k are before elements > k.
time: O(n)
"""

def relocate_func(data, index, k):
    if index >= len(data):
        return data
    else:
        if data[index] <= k:
            value = data.pop(index)
            data = [value] + data
        
        data = relocate_func(data, index+1, k)
        return data


def relocate(data, k):
    return relocate_func(data.copy(), 0, k)


if __name__ == '__main__':
    data = [1, 3, 0, -10, 78, 90, 56, 32, 8, -1]
    print(data)
    print(relocate(data, 5))
    print(relocate(data, 51))
    print(relocate(data, 2))
