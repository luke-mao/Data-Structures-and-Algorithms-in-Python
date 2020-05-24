"""
R, S and T, three non-empty stack.
Transfer all elements of S to T, in the same order. 
R remain unchanged.
(this question is very easy)
"""

from example_stack import ArrayStack

def transfer(R, S, T):
    """put everything of S to R, then pop to T"""
    R_top = R.top()

    while not S.is_empty():     R.push(S.pop())
    while R_top != R.top():     T.push(R.pop())


if __name__ == '__main__':
    
    R = ArrayStack()
    for i in range(1, 3+1):     R.push(i)

    S = ArrayStack()
    S.push(4)
    S.push(5)

    T = ArrayStack()
    for i in range(6, 9+1):     T.push(i)

    print("original:")
    R.show()
    S.show()
    T.show()

    transfer(R, S, T)

    print("\nafter:") 
    R.show()
    S.show()
    T.show()