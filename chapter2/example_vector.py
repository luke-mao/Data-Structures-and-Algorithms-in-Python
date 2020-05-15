"""
textbook example: class Vector
"""

class Vector:
    """ Represent a vector in a multi-dimensional space"""

    def __init__(self, d):
        if not d >= 1:
            raise ValueError("Dimension number must >= 1")

        self._coordinates = [0] * d
    
    def __len__(self):
        return len(self._coordinates)
    
    def __getitem__(self, j):
        if j < -len(self._coordinates) or j >= len(self._coordinates):      # index can be negative
            raise ValueError("Index out of bound")

        return self._coordinates[j]
    
    def __setitem__(self, j, val):
        if j < -len(self._coordinates) or j >= len(self._coordinates):      # index can be negative
            raise ValueError("Index out of bound")
        if not isinstance(val, (int, float)):
            raise ValueError("Input value must be either int or float")
            
        self._coordinates[j] = val
    
    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Dimension must be equal")

        result = Vector(len(self))          # use the __init__
        for j in range(len(self)):  
            result[j] = self[j] + other[j]  # use __getitem__  
        return result
    
    def __eq__(self, other):
        return self._coordinates == other._coordinates
    
    def __ne__(self, other):
        return self._coordinates != other._coordinates
    
    def __str__(self):
        return "<{}>".format(','.join([str(i) for i in self._coordinates]))



if __name__ == '__main__':
    v = Vector(5)
    v[1] = 23
    v[-1] = 45
    v[2] = 50
    print(str(v))
    print(v[2])

    u = v + v
    print(str(u))

    print(u == u)
    
    # g = Vector(0)

