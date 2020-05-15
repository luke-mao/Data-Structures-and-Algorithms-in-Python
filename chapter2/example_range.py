class Range:
    """ a class that mimic's the built-in range class """

    def __init__(self, start, stop=None, step=1):
        """several forms
        Range(5)
        Range(5, 10)
        Range(5, 10, 2)
        """

        if stop == None:
            start, stop = 0, start
        
        if step == 0:
            raise ValueError("Step cannot be 0")
        
        self._start, self._stop, self._step = start, stop, step     # assign values
        self._length = max(0, (stop-start+step-1)//step)

    def __len__(self):
        return self._length
    
    def __getitem__(self, k):
        # consider negative k
        if k < 0: k += len(self)
        if k < 0 or k >= len(self): raise ValueError("Index not in range")
        
        return self._start + k * self._step


if __name__ == '__main__':
    
    # this class has the index error problem
    # if cancel the condition test on k: then the program goes to infinite
    for i in Range(5):
        print(i)
        