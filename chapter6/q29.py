"""
write a feature, queue.rotate(),
it takes the first value out from the queue and insert back to the queue,
but do not use queue.enqueue and queue.dequeue
"""

from example_queue import ArrayQueue

class ArrayQueue_2(ArrayQueue):

    def rotate(self):
        if not self.is_empty():
            tmp = self._data[self._front]   # copy the first value
            self._data[self._front] = None  # same as dequeue
            self._front += 1                # front increase 1
            self._data[(self._front + self._num - 1) % self._capacity] = tmp    # note the -1 !!


if __name__ == '__main__':
    q = ArrayQueue_2()
    for i in range(10):
        q.enqueue(i)
    print("original: ")
    q.show()
    print()

    for _ in range(5):
        print("rotate {}".format(q.first()))
        q.rotate()
        q.show()
    
