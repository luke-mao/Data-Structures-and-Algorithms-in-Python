def is_even(k):
    '''
    return True if k is an even number,
    no multiply, division or mod
    '''
    return k & 1 == 0


if __name__ == '__main__':
    print ("{}: {} is even".format(is_even(3), 3))
    print ("{}: {} is even".format(is_even(0), 0))
    print ("{}: {} is even".format(is_even(6), 6))
    print ("{}: {} is even".format(is_even(-4), -4))
    print ("{}: {} is even".format(is_even(-5), -5))
