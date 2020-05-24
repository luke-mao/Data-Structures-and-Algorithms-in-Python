"""
Use two stacks to accomplish queue ADT.

This implication uses a reverse_flag to determine if the first element is at the bottom of stack (true) or top(false).
The reverse flag is updated during "enqueue" and "first".
Using the flag, time complexity of essential features are:
    first, dequeue, enqueue: O(1) or O(n), 50% probability.

A better design please see Q25_2.py, so that first and dequeue are O(1) and enqueue is O(n)
"""

from example_stack import ArrayStack
from example_stack import Empty

class ArrayQueueUseTwoStacks:
    """
    use two stacks to demonstrate a queue,
    "show" is not included in the task for simplicity.
    """

    def __init__(self):
        self._a = ArrayStack()
        self._b = ArrayStack()
        self._num = 0
        self._reverse_flag = True       # True means the first element is at the bottom of the stack

    def __len__(self):
        return self._num

    def is_empty(self):
        return self._num == 0

    def first(self):
        if self._num == 0:  
            raise Empty("queue is empty")
        else:
            if self._reverse_flag:  
                # the first element is at the bottom of the stack
                # move everything of stack a to stack b, return the top
                while not self._a.is_empty():
                    self._b.push(self._a.pop())
                
                # swap two stacks
                self._a, self._b = self._b, self._a
                self._reverse_flag = False
            
            else:
                # the first element is at the top of stack a
                self._reverse_flag = True

            return self._a.top()
    

    def enqueue(self, value):
        # put a value into the stack, using push
        self._num += 1

        if self._reverse_flag:  # if the first element is at the bottom of stack a
            self._a.push(value)
        
        else:   # the first element is at the top of stack a
            # need to push to b first, then move everything from a to b
            self._b.push(value)
            
            while not self._a.is_empty():
                self._b.push(self._a.pop())
            
            # swap two stacks
            self._a, self._b = self._b, self._a

    
    def dequeue(self):
        # return the first value
        
        if self._num == 0:
            raise Empty("queue is empty")
        else:
            self._num -= 1

        if self._reverse_flag:  # the first element is at the bottom of stack a:
            # move to b, then pop, remember to swap and change the flag
            while not self.is_empty():
                self._b.push(self._a.pop())
            
            value = self._b.pop()

            self._a, self._b = self._b, self._a
            self._reverse_flag = False

            return value

        else:
            return self._a.pop()


if __name__ == '__main__':
    
    q = ArrayQueueUseTwoStacks()
    print("initally, check if queue is empty: ", q.is_empty())
    
    print("put 0 to 29 into the queue")
    for i in range(30):     q.enqueue(i)

    print("length of queue: ", len(q))
    print("first value: ", q.first())

    print("dequeue 25 elements")
    for _ in range(25):     print(q.dequeue())

    print("check length: ", len(q))
    print("check first: ", q.first())

    
