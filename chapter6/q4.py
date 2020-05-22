"""
recursion, empty the stack
"""
from example_stack import ArrayStack

def empty_stack(S):
    if S.is_empty():
        return
    else:
        S.pop()
        empty_stack(S)
        return


if __name__ == '__main__':
    S = ArrayStack()
    for i in range(30): S.push(i)
    S.show()

    empty_stack(S)
    S.show()