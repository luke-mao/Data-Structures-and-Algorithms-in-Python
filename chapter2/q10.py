from example_vector import Vector

class Vector_q10(Vector):
    def __neg__(self):
        
        result = Vector_q10(len(self))
        
        for j in range(len(result)):
            result[j] = -1 * self[j]
        return result


if __name__ == '__main__':
    v = Vector_q10(5)
    v[1] = 23
    v[-1] = 45
    v[2] = 50
    print(str(v))
    print(v[2])

    print(str(-v))
        
