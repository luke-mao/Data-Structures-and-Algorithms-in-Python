"""
input 3 integers from the stdin, a,b,c
determine if they satisfy one of the following equations:
a+b=c, a=b-c or a*b=c
"""

def check(a,b,c):
    if a + b == c:
        return True
    if a == b - c:
        return True
    if a * b == c:
        return True
    
    return False


if __name__ == '__main__':
    try:
        num = input("Input three integers, split by comma: ")
        num_list = num.split(",")
        a, b, c = int(num_list[0]), int(num_list[1]), int(num_list[2])
        print(check(a,b,c))
    except ValueError:
        print("Please input three integers!!")
    
    
