"""
use randint to write the shuffle function
"""
import random

def my_shuffle(data):
    data2 = data[:]
    result = []
    while len(data2) != 0:
        index = random.randint(0, len(data2)-1)      # randint: include the two end points
        result.append(data2.pop(index))

    return result
    

if __name__ == '__main__':
    data = [1,4,7, 10, 0, 6]
    print(my_shuffle(data))