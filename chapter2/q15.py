from example_vector import Vector

class Vector_q15(Vector):

    def __init__(self, d):

        if isinstance(d, int):
            return super().__init__(d)
        elif isinstance(d, list):
            self._coordinates = d
        else:
            raise TypeError("d can be only int or list")


if __name__ == '__main__':
    v = Vector_q15(5)
    v[1] = 23
    v[-1] = 45
    v[2] = 50
    print(str(v))

    v2 = Vector_q15([5, 3, 1])
    print(str(v2))
    print(len(v2))
