# recursion, find max value among a list with n entries

def find_max(data):
    """
    linear recursion: time O(n), space O(n)
    """
    if len(data) == 1:
        return data[0]
    else:
        return max(data[0], find_max(data[1:]))


def find_max2(data, left, right):
    """
    recursion, idea from binary search.
    after each execution, the space of range halves, so the space is O(log n).
    total n numbers, so need 2*n - 1 execution, so time is O(n)
    """
    if left >= right:
        return data[left]
    else:
        mid = (left + right) // 2
        return max(
            find_max2(data, left, mid-1), 
            data[mid], 
            find_max2(data, mid+1, right)
        )





if __name__ == '__main__':
    data = [1, 5, 10, 30, 6, 7, 100, 50, 400, 0, -50]
    # print(find_max(data))
    print(find_max2(data, 0, len(data)-1))