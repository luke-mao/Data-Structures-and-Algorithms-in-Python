"""
natural join two sets, (x,y) and (y,z) => (x,y,z).

method:
    use map(dictionary)
"""

def natural_join(data1, data2):
    """data 1 and 2 in the format of tuples in list"""
    Ymap = {}
    for x, y in data1:
        if y not in Ymap:
            Ymap[y] = [x]
        else:
            Ymap[y].append(x)
    
    result = []
    for y, z in data2:
        if y in Ymap:
            for x in Ymap[y]:
                result.append((x, y, z))
    
    return result


if __name__ == '__main__':
    data1 = [
        (3,4),
        (5,6),
        (7,8)
    ]

    data2 = [
        (4,9),
        (5,10),
        (6,11),
        (6,13),
        (6,20)
    ]

    print(natural_join(data1, data2))


"""
the time complexity is O(n+m),
since need linear scan of both data1 and data2
"""