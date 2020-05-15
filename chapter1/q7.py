def square_odd_sum(n):
    if (not isinstance(n, int)) or (n <= 0):
        return "Error: n is a positive integer"
    
    total = sum(i*i for i in range(1, n+1, 2))
    
    return total


if __name__ == '__main__':
    print("Input {}: {}".format(-5, square_odd_sum(-5)))
    print("Input {}: {}".format(10, square_odd_sum(10)))
    print("Input {}: {}".format(3, square_odd_sum(3)))