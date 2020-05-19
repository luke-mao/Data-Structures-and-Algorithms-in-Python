"""
q20: time O(log n)
"""

def relocate_func(data, left, right, k):
    """
    change the value in place.
    left and right: index
    k: value for comparison
    """

    if left >= right:
        return data
    else:
        if data[left] > k and data[right] <= k:                 # swap
            data[left], data[right] = data[right], data[left]
            return relocate_func(data, left+1, right-1, k)

        elif data[left] <= k and data[right] > k:              
            return relocate_func(data, left+1, right-1, k)
        
        elif data[left] <= k and data[right] <= k:
            # append data[right] to the front of the list
            val = data.pop(right)
            data = [val] + data
            return relocate_func(data, left+2, right, k)

            
        elif data[left] > k and data[right] > k:
            # append data[left] to the back of the list
            val = data.pop(left)
            data = data + [val]
            return relocate_func(data, left, right-2, k)
            

def relocate(data, k):
    return relocate_func(data.copy(), 0, len(data)-1, k)


if __name__ == '__main__':
    data = [1, 3, 0, -10, 78, 90, 56, 32, 8, -1]
    print(data)
    print(relocate(data, 5), 5)
    print(relocate(data, 51), 51)
    print(relocate(data, 2), 2)
    print(relocate(data, 3), 3)

