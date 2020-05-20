from example_dynamic_array import DynamicArray

class DynamicArray3(DynamicArray):

    def insert(self, k, value):
        if not (k >= 0  and k <= self._n):
            raise IndexError("Invalid index {}".format(k))

        # first construct the empty array if the array is full
        if self._n == self._capacity:
            self._capacity *= 2

        B = self._make_array(self._capacity)

        # copy the elements that before the k
        self._n += 1
        B[:k] = self._A[:k]
        B[k] = value
        B[k+1:self._n] = self._A[k:self._n-1]   # !! the index of self._A

        self._A = B
    
    def __str__(self):
        return " ".join(str(self._A[i]) for i in range(self._n))


if __name__ == '__main__':
    a = DynamicArray3()

    for i in range(20):
        a.append(i)
    
    print(str(a))
    a.insert(k=0, value=50)
    print(str(a))
    a.insert(k=5, value=60)
    print(str(a))
    a.insert(k=22, value=70)
    print(str(a))