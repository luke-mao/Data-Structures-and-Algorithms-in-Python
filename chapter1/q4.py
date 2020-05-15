def square_sum(n):
    '''
    n is a positive integer, return the square sum from 1 to n
    '''
    if (not isinstance(n, int)) or (n <= 0):
        return "Error: n is a positive integer"
    
    sumV = 0
    for i in range(1, n+1):
        sumV += i * i
    
    return sumV 


if __name__ == '__main__':
    print("Input {}: {}".format(-5, square_sum(-5)))
    print("Input {}: {}".format(10, square_sum(10)))
    print("Input {}: {}".format(3, square_sum(3)))