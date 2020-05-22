"""
transfer(S, T): transfer elements in S to T,
the top element in S will be in the bottom of T
"""

from example_stack import ArrayStack
from example_stack import Empty

def transfer(S, T):
    while not S.is_empty():
        T.push(S.pop())
    

if __name__ == '__main__':
    S = ArrayStack()
    for i in range(10): S.push(i)
    S.show()

    T = ArrayStack()
    transfer(S, T)

    print("S")
    S.show()

    print("T")
    T.show()
