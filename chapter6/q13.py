"""
a deque with sequence (1,2,3,4,5,6,7,8).
given a queue, 
use only the deque and queue,
to shift the sequence to the order (1,2,3,5,4,6,7,8)
"""

from example_queue import ArrayQueue
from example_double_ended_queue import ArrayDoubleEndedQueue

D = ArrayDoubleEndedQueue()
for i in range(1, 8+1):     D.add_last(i)

Q = ArrayQueue()

print("initially")
D.show()
Q.show()
print()

# shift the order
for _ in range(3):  D.add_last(D.delete_first())
Q.enqueue(D.delete_first())
D.add_last((D.delete_first()))
D.add_last(Q.dequeue())
for _ in range(3):  D.add_last(D.delete_first())

print("finally")
D.show()
Q.show()