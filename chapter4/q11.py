def unique(data):
    if len(data) == 1:
        return True
    else:
        if unique(data[1:]):
            for value in data[1:]:
                if value == data[0]: return False
            return True
        else:
            return False


if __name__ == '__main__':
    data = [1, 5, 2, 3, 5, 7]
    data2 = [50, 0, 1, 4, 6, 2]
    print(unique(data))
    print(unique(data2))