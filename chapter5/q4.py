from example_dynamic_array import DynamicArray

class DynamicArray2(DynamicArray):

    def __getitem__(self, k):

        if k >= 0  and k < self._n:
            return super().__getitem__(k)
        elif k < 0 and k >= -1 * self._n:
            k += self._n
            return super().__getitem__(k)
        else:
            raise IndexError("Invalid index")


if __name__ == '__main__':
    
    a = DynamicArray2()
    
    for i in range(30): # insert 0 ... 29, total 30 numbers
        a.append(i)
    
    print(a[5])
    print(a[-1])
    print(a[-2])
    print(a[-30])
    # print(a[-50])