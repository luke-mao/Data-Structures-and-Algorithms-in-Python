def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high)//2
        if data[mid] == target:
            return True
        elif data[mid] > target:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)

