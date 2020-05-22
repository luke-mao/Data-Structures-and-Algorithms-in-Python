"""
check the efficiency of list.remove,
compare the time to remove the first, middle and last element
"""

import time

def test(length):
    data = [i for i in range(length)]

    t1 = time.time()
    data.remove(0)
    t2 = time.time()
    data.remove(length//2)
    t3 = time.time()
    data.remove(length-1)
    t4 = time.time()

    return int((t2-t1)*10**6), int((t3-t2)*10**6), int((t4-t3)*10**6)


if __name__ == '__main__':
    
    length_list = [10**4, 10**5, 10**6, 10**7]
    time1 = 0
    time2 = 0
    time3 = 0
    for length in length_list:
        for _ in range(5):      # each length do 5 times, then take the average
            t1, t2, t3 = test(length)
            time1 += t1
            time2 += t2
            time3 += t3
        
        print("length={}, remove first = {}, remove mid = {}, remove last = {}, unit 10^-6 s".format(length, time1, time2, time3))


"""
linear search, remove the last element takes the longest time. 
"""