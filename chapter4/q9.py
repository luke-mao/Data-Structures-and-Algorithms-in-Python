# a simple recursion, no loop, find the min and max among a list of data
# time, space both are O(n)

def find(data):
    if len(data) == 1:
        return (data[0], data[0])
    else:
        (minV, maxV) = find(data[1:])
        return (min(data[0], minV), max(data[0], maxV))


if __name__ == '__main__':
    data = [-5, 6, 7, 10, 70, -90, 18, 6]
    data2 = [700, 98, 800, -50, 0, 18, 2, 2000]
    print(find(data))
    print(find(data2))