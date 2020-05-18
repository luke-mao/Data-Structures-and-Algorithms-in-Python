def harmonic(n):
    
    if n == 1:
        return 1
    else:
        return 1.0 / n + harmonic(n-1)


if __name__ == '__main__':
    print(harmonic(3))