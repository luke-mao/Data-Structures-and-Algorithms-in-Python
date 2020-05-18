def power(x, n):
    # calculate x^n
    if n == 1:
        return x
    else:
        return x * power(x, n-1)


def power2(x, n):
    if n == 1:
        return x
    else:
        partial = power2(x, n//2)
        result = partial * partial
        if n % 2 == 1: result *= x
        
        return result