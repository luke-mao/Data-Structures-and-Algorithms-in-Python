from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):

    @abstractmethod
    def __len__(self):
        """return the length"""
        pass

    @abstractmethod
    def __getitem__(self, i):
        """return the element at this index i"""
        pass

    def __contains__(self, val):
        """check if contain this value"""
        for i in range(len(self)):
            if self[i] == val: return True
        
        return False
    
    def index(self, val):
        """return the leftmost index >= 0 at which val is found,
           or raise ValueError"""
        
        for j in range(len(self)):
            if self[j] == val: return j
        
        raise ValueError("value not in sequence")

    def count(self, val):
        """return the number of elements equal to this value"""
        counter = 0
        for j in range(len(self)):
            if self[j] == val: counter += 1
        
        return counter 

