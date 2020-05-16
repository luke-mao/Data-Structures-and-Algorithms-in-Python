# same as q12

from example_vector import Vector

class Vector_q13(Vector):

    def __mul__(self, coef):
        
        result = Vector_q13(len(self))
        
        for i in range(len(self)):
            result[i] = coef * self[i]
        
        return result
    
    def __rmul__(self, coef):
        return self * coef


if __name__ == '__main__':

    v = Vector_q13(5)
    v[1] = 23
    v[-1] = 45
    v[2] = 50
    print(str(v))

    u1 = 3 * v
    u2 = v * 3
    print(str(u1))
    print(str(u2))