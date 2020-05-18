# textbook example of factorial calculation

def factorial(n):
    if n == 0:      # end condition
        return 1
    else:
        return n * factorial(n-1)   # recursion

