"""
same question as q13, but use the deque and a stack
"""

from example_double_ended_queue import ArrayDoubleEndedQueue
from example_stack import ArrayStack

D = ArrayDoubleEndedQueue()
for i in range(1, 8+1):     D.add_last(i)
S = ArrayStack()

print("initially")
D.show()
S.show()
print()

for _ in range(3):  D.add_last(D.delete_first())
for _  in range(2): S.push(D.delete_first())
for _  in range(2): D.add_last(S.pop())
for _ in range(3):  D.add_last(D.delete_first())

print("finally")
D.show()
S.show()