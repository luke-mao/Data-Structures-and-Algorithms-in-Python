"""
reverse polish notation:
no recursion
"""

from example_stack import ArrayStack

def reverse_polish_notation(string):
    # first check if all brackets are matched, using a stack
    s = ArrayStack()

    bracket_left = ["(", "[", "{"]
    bracket_right = [")", "]", "}"]

    for char in string:
        if char in bracket_left:    
            s.push(bracket_left.index(char))
        
        elif char in bracket_right:
            if s.top() != bracket_right.index(char):
                raise ValueError("bracket does not match")
            else:
                s.pop()
        else:       # for digits and other operation symbol
            continue
    
    if not s.is_empty():
        raise ValueError("bracket does not match")

    pass

