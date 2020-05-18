def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fibonacci2(n):
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = fibonacci2(n-1)
        return (a+b, a)
