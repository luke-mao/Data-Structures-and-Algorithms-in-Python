from example_vector import Vector

class Vector_q11(Vector):

    def __radd__(self, other):
        return super().__add__(other)
        # or you can write: return self + other


if __name__ == '__main__':
    v = Vector_q11(5)
    v[1] = 23
    v[-1] = 45
    v[2] = 50
    print(str(v))

    u1 = [1,2,3,4,5] + v 
    u2 = v + [1,2,3,4,5]

    print(str(u1))
    print(str(u2))
        
    