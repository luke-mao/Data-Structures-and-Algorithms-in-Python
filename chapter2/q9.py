from example_vector import Vector

class Vector_q9(Vector):

    def __init__(self, d):
        super().__init__(d)
    
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("Dimension must be equal")

        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        
        return result


if __name__ == '__main__':
    v = Vector_q9(5)
    v[1] = 23
    v[-1] = 45
    v[2] = 50
    print(str(v))
    print(v[2])

    u = v + v
    print(str(u))

    print(u == u)

    z = v - v 
    print(str(z))