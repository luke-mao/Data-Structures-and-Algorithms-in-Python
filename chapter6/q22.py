"""
reverse polish notation:
no recursion
"""

from example_stack import ArrayStack
from example_stack import Empty

def reverse_polish_notation(equation):
    
    # define all operators and brackets
    bracket_left = ["(", "[", "{"]
    bracket_right = [")", "]", "}"]
    operator = ["+", "-", "*", "/"]
    
    # first check if all brackets are matched, using a stack
    s = ArrayStack()

    for char in equation:
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

    
    """
    now do the reverse polish notation:
    1. read the input char by char, push into the stack
    2. if meet close bracket, pop all elements including the starting bracket
    3. then place the operands together, followed by the operator.
    4. push the result back to the stack, and continue step 1.
    5. when reading finish, pop all elements out and do step 3 again.
    """

    s = ArrayStack()    # re-initialize
    number = ""

    for char in equation:

        if char.isnumeric():
            number += char

        elif (char in operator) or (char in bracket_left) or (char in bracket_right):
            if len(number) != 0:
                s.push(number)
                number = ""

            if char in bracket_right:
                try:
                    operand2 = s.pop()
                    operator_here = s.pop()
                    operand1 = s.pop()
                    
                    s.pop()     # pop the starting bracket

                    s.push(operand1 + operand2 + operator_here)
                except:
                    raise ValueError("invalid equation {}".foramt(equation))
            
            else:               # char in bracket_left or in operator
                s.push(char)

        else:
            raise ValueError("invalid symbol {}".format(char))

    # at the end of the loop, check how many left
    if len(number) != 0:
        s.push(number)

    value_left = [s.pop()]
    while not s.is_empty():
        value_left.append(s.pop())
    
    if len(value_left) == 1:
        return value_left[0]
    elif len(value_left) == 3:
        return value_left[2] + value_left[0] + value_left[1]
    else:
        raise ValueError("invalid equation {}".format(value_left))


if __name__ == '__main__':

    eq = [
        "7+3", "6/2", "3-9", "4*8",
        "(7+3)*(4-8)", "(6*7)/(5-2)",
        "((5+2)*(8-3))/4"
    ]

    for each in eq:
        print("{} => {}".format(each, reverse_polish_notation(each)))