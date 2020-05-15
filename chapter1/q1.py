def is_multiple(n, m):
    '''
    if n = m * i, then return True, else return False
    '''

    if n == 0 and m == 0:
        return True
    elif m == 0:
        return False
    elif n % m == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print("{}: {} is a multiple of {}".format(is_multiple(4, 8), 4, 8))
    print("{}: {} is a multiple of {}".format(is_multiple(8, 4), 8, 4))
    print("{}: {} is a multiple of {}".format(is_multiple(0, 0), 0, 0))
    print("{}: {} is a multiple of {}".format(is_multiple(0, 5), 0, 5))
    print("{}: {} is a multiple of {}".format(is_multiple(5, 0), 5, 0))
    print("{}: {} is a multiple of {}".format(is_multiple(-2, 2), -2, 2))