def minmax(data):
    '''
    return a tuple (min, max), but cannot use default min and max functions
    '''
    minV, maxV = data[0], data[0]
    for value in data[1:]:
        if value < minV: minV = value
        if value > maxV: maxV = value
    
    return (minV, maxV)


if __name__ == '__main__':
    data = [1, 5, -9, 6, 7]
    print("minV = {}, maxV = {}".format(minmax(data)[0], minmax(data)[1]))
    