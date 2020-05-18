"""
only use + and //, write a recursion, calculate the integer part of log2(n).
example:
    log2(50) => 5
    log2(31) => 4
    log2(32) => 5
    log2(1) => 0
    log2(16) => 4
# the input n should be > 0
"""

def log2(n):
    """
    return the integer part of the answer.
    method: count how many times can // 2, the solution >= 1    
    """
    if n < 0:       raise ValueError("Wrong input") 
    elif n == 0:    return 0
    elif n == 1:    return 0
    else:           return 1 + log2(n//2)       # here has 1 already, so n == 1 return 0



if __name__ == '__main__':
    print(log2(50))
    print(log2(1000))
    print(log2(500))

