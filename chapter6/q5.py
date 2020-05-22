"""
inversion a list using stack
"""

from example_stack import ArrayStack

def reverse_list(data):
    # modify the list in place
    if len(data) <= 1:
        return
            
    S = ArrayStack()
    for each in data:
        S.push(each)
    
    for i in range(len(data)):
        data[i] = S.pop()


if __name__ == '__main__':

    data = [1,2,4,6,7,5,10]
    print(data)
    reverse_list(data)
    print(data)

    data2 = [3]
    print(data2)
    reverse_list(data2)
    print(data2)