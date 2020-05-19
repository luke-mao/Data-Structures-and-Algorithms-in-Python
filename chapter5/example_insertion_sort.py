def insertion_sort(data):
    """ascending order"""
    for k in range(len(data)):
        current = data[k]
        j = k
        while  j > 0  and current < data[j-1]:
            data[j] = data[j-1]
            j -= 1
            
        data[j] = current

    return data

if __name__ == '__main__':
    data = [3, 6, 1, 2, 4]
    print(insertion_sort(data.copy()))