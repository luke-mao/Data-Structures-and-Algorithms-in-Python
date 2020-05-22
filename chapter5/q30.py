"""
known how many numbers n to sort.
receive the numbers in random order.
use insertion sort, best case is O(n), worst case is O(n^2)
"""

def insertion_sort(data):
    """ascending sort"""
    for k in range(1, len(data)):
        if data[k] is not None:
            current = data[k]
            j = k

            # if "current" is smaller, move it forward
            while j > 0 and current < data[j-1]:
                # empty a space for the smaller "current"
                data[j] = data[j-1]
                j -= 1
            data[j] = current


if __name__ == '__main__':

    # given n
    n = 10
    data = [None] * 5

    data[0] = 5
    print(data)

    data[1] = 3
    insertion_sort(data)
    print(data)

    data[2] = 7
    insertion_sort(data)
    print(data)

    data[3] = 4
    insertion_sort(data)
    print(data)
    
    data[4] = 6
    insertion_sort(data)
    print(data)


        

    