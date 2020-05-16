"""different with q12 and 13, now code the vector dot product"""

from example_vector import Vector

class Vector_q14(Vector):

    def __mul__(self, other):
        
        if isinstance(other, (int, float)):
            result = Vector_q14(len(self))
            for i in range(len(result)): result[i] = other * self[i]
            return result 
        
        else:
            if len(self) != len(other): 
                raise ValueError("Dimension not equal")
            else:
                result = sum([self[i]*other[i] for i in range(len(self))])
                return result
    
    def __rmul__(self, other):
        return self * other 


if __name__ == '__main__':
    v = Vector_q14(5)
    v[1] = 23
    v[-1] = 45
    v[2] = 50
    print(str(v))

    # test scalar
    u1 = 3 * v 
    u2 = v * 3
    print(str(u1))
    print(str(u2))

    # test vector
    u = [1,2,3,4,5]
    print(u * v)
    print(v * u)

    

