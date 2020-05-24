"""
double ended queue ADT, 
same as example_double_ended_queue.py
"""

from example_double_ended_queue import ArrayDoubleEndedQueue

if __name__ == '__main__':
    q = ArrayDoubleEndedQueue()

    for i in range(30):
        if i % 2 == 0:
            q.add_first(i)
        else:
            q.add_last(i)

    print("initial: insert 30 numbers")
    q.show()

    print("delete first 10 and last 10")
    for _ in range(10):
        print(q.delete_first())
        print(q.delete_last())
    
    
    q.show()
    print("length {}".format(len(q)))

    print("first value: {}".format(q.first()))
    print("last value: {}".format(q.last()))
    print("is empty: {}".format(q.is_empty()))