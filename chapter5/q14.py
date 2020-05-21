"""
use random.randrange(n) to model the function of random.shuffle(list).
random.shuffle shuffles the list in place, 
here i will return a new list
"""

import random

def shuffle(data):
    result = data[:]
    for i in range(len(data)-1):
        index = random.randrange(i, len(data))      # i <= index < len(data)
        result[i], result[index] = result[index], result[i]
    
    return result


if __name__ == '__main__':

    data = [1,2,3,4,5]
    n = 10000           # test times

    statistics = [0] * 5    # count the numbers of the value "2" on each position


    for _ in range(n):
        result = shuffle(data)
        index = result.index(2)     # find the value "2" index
        statistics[index] += 1
    
    for i in range(len(statistics)):
        print("P(Number 2 on {} position) = {}%".format(i+1, statistics[i]/sum(statistics)*100))
