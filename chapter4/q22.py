"""
quick way to find power(x, n),
no recursion
"""

# does not quite understand???
def power(x, n):
    """both x and n are positive integers"""
    if n == 0:      return 1
    elif n == 1:    return x
    else:
        # find 2^k that is greater than n
        k = 0
        while (1<<k) <= n:   k += 1

        k -= 1  # so 2^k is slightly less than 1

        answer = 1
        for j in range(k, -1, -1):      # j start from k, then k-1, k-2 ... 0
            answer = answer ** 2
            if (1<<j) & n > 0:
                answer *= x
        
        return answer


def power_with_recursion(x, n):
    if n == 0:
        return 1
    else:
        partial = power_with_recursion(x, n//2)
        p = partial * partial
        if n % 2 == 1:
            p *= x
        return p


if __name__ == '__main__':
    print(power_with_recursion(3, 4), 3**4)
    print(power_with_recursion(4, 5), 4**5)
    print(power_with_recursion(2, 9), 2**9)
    print(power_with_recursion(2, 0), 2**0)
    print(power_with_recursion(2, 1), 2**1)

    print(power(3, 4), 3**4)
    print(power(4, 5), 4**5)
    print(power(2, 9), 2**9)
    print(power(2, 0), 2**0)
    print(power(2, 1), 2**1)