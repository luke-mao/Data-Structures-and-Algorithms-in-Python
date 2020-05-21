"""
write the function of pop() or pop(index) in the DynamicArray,
and also decreases 50% of the size when element numbers decreases to N//4
"""

from example_dynamic_array import DynamicArray

class DynamicArray2(DynamicArray):
    """dynamic array, add pop and associated resizing method"""

    def pop(self, index=None):
        """
        default method: pop the last element and return
        but user can also pop index any index in the valid range,
        supports negative index
        """
        if index is None:   index = self._n - 1
        if index < 0:       index += self._n
        if not (index >= 0 and index < self._n):
            raise IndexError("invalid index")
        
        returnV = self._A[index]

        if index == self._n:
            self._n -= 1
        
        else:
            # the index is around the middle
            B = self._make_array(self._capacity)
            B[:index] = self._A[:index]
            B[index:self._n-1] = self._A[index+1:self._n]   # careful about the index
            
            self._n -= 1
            self._A = B
        

        # now check if need to decreases the capacity
        if self._n <= self._capacity // 4:
            # need to downgrade the size
            self._capacity = self._capacity // 4
            B = self._make_array(self._capacity)
            B[:self._n] = self._A[:self._n]
            self._A = B
        
        return returnV


    def __str__(self):
        """use in the str(xxx)"""
        return " ".join(str(self._A[i]) for i in range(self._n))


if __name__ == '__main__':

    a = DynamicArray2()
    for i in range(20):
        a.append(i)
    print(str(a))

    print(a.pop(19))
    print(str(a))
    
    print(a.pop(5))
    print(str(a))

    print(a.pop(0))
    print(str(a))


    for i in range(15, -1, -1):
        a.pop(i)
        print(str(a))


