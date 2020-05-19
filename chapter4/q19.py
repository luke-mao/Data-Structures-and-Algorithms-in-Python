def func(data, index):
    if index >= len(data):
        return data
    else:
        if data[index] & 1 == 0:    # even number
            value = data.pop(index)
            data = [value] + data
        
        data = func(data, index+1)
        return data


def relocate(data):
    return func(data, 0)


if __name__ == '__main__':
    data = [
        [3,5,6,7,8,9],
        [3, 5, 7, 90, 6, 4, 2, 0],
        [2],
        [5],
        [5, 7]
    ]

    for i in data:
        print(relocate(i))



