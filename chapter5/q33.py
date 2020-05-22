"""
a class Matrix2D, function including add and multiply
"""

class Matrix2D:
    """a class matrix2D, function: add and multiply"""

    def __init__(self, data):
        
        ok = self._check(data)
        if not ok:
            raise ValueError("the input data is invalid, check size")
        
        self._row_number, self._col_number = len(data), len(data[0])
        self._data = data


    def _check(self, data):
        """check the size is valid, including row and column, scan the data"""
        row, col = len(data), len(data[0])
        for each_row in data:
            if len(each_row) != col:
                return False
        
        return True
    

    # three functions for addition, add, radd, iadd
    def __add__(self, other):
        """add 2 2D array together, require the size must be equal"""
    
        if self._row_number != other._row_number or self._col_number != other._col_number:
            raise ValueError("Addition: invalid size")

        result = [[None]*self._col_number for _ in range(self._row_number)]

        for i in range(self._row_number):
            for j in range(self._col_number):
                result[i][j] = self._data[i][j] + other._data[i][j]
        
        return Matrix2D(result)
    
    def __radd__(self, other): return self + other

    def __iadd__(self, other): return self + other


    # three functions for multiplication
    def __mul__(self, other):

        if isinstance(other, (int, float)):
            
            result = [[None]*self._col_number for _ in range(self._row_number)]
            
            for i in range(self._row_number):
                for j in range(self._col_number):
                    result[i][j] = self._data[i][j] + other._data[i][j]

            return Matrix2D(result)
        
        elif isinstance(other, Matrix2D):

            # condition: self._col = other._row
            if self._col_number != other._row_number:
                raise ValueError("Multiplication: invalid size")

            result = [[None]*other._col_number for _ in range(self._row_number)]

            for i in range(len(result)):
                for j in range(len(result[0])):
                    # result[i][j] = self[i]row * other[j]col and then sum together
                    result[i][j] = 0
                    for k in range(self._col_number):
                        result[i][j] += self._data[i][k] * other._data[k][j]
            
            return Matrix2D(result)
        
        else:
            raise ValueError("Multiplication: invalid type")

    def __rmul__(self, other):  return other.__mul__(self)      # !!!

    def __imul__(self, other):  return self * other


    # for printing, need to return a string
    def __str__(self):
        string = "\n".join((" ".join(str(i) for i in row)) for row in self._data)
        return string


    def printout(self):
        print(self._data)


if __name__ == '__main__':

    data_list = [
        [[1,2,3],[4,5,6]],
        [[1,2],[3,4],[5,6]],
        [[1],[2],[3]],
        [[2,5,0],[4,1,6]],
    ]

    matrix_list = [None] * len(data_list)

    for i in range(len(data_list)):
        matrix_list[i] = Matrix2D(data_list[i])
        print(str(matrix_list[i]))
        print()

    # test addition
    print("test addition a + d")
    t1 = matrix_list[0] + matrix_list[3]
    t2 = matrix_list[3] + matrix_list[0]
    matrix_list[0] += matrix_list[3]

    print(str(t1), "\n")
    print(str(t2), "\n")
    print(str(matrix_list[0]), "\n")
    matrix_list[0] = Matrix2D(data_list[0])     # change back to the original
    del t1, t2


    # test multiplication
    print("test multiplication a and b")
    t1 = matrix_list[0] * matrix_list[1]
    matrix_list[0] *= matrix_list[1]
    print(str(t1), "\n")
    print(str(matrix_list[0]), "\n")
    matrix_list[0] = Matrix2D(data_list[0])     # change back to the original
    del t1

    # test multiplication
    print("test multiplication a and c")
    t1 = matrix_list[0] * matrix_list[2]
    matrix_list[0] *= matrix_list[2]
    print(str(t1), "\n")
    print(str(matrix_list[0]), "\n")
    matrix_list[0] = Matrix2D(data_list[0])     # change back to the original

    # test multiplication: invalid size
    # print("test multiplication, invalid size, a and d")
    # t1 = matrix_list[0] * matrix_list[3]
