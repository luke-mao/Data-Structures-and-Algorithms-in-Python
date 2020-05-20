import ctypes   # provide low level arrays
import sys

class DynamicArray:
    """a dynamic array class akin to a simplified python list"""

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
    
    def _make_array(self, length):
        return (length * ctypes.py_object)()
    
    def __len__(self):
        return self._n  # the length
    
    def __getitem__(self, k):
        if not (k >=0 and k <= self._n):
            raise IndexError("invalid index")
        return self._A[k]
    
    def append(self, obj):
        if self._n == self._capacity:   # need to increase size
            self._resize(2*self._capacity)  # double the size every time when full
        self._A[self._n] = obj
        self._n += 1
    
    def _resize(self, length):
        B = self._make_array(length)    # another array
        for i in range(self._n):
            B[i] = self._A[i]
        
        self._A = B
        self._capacity = length


if __name__ == '__main__':
    a = DynamicArray()
    
    for i in range(30):
        # the size does not change, probably due to the "pointer"
        print("length {}, Size in bytes {}".format(len(a), sys.getsizeof(a))) 
        a.append(i)
    
    print(a[5])
    # print(a[-1])  # does not support negative index
    
