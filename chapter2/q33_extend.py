"""
q33 extend version:
file q33.py constructs a class Polynomial that can take a polynomial as input, 
and decompose this polynomial, and also calculate the first order derivative. 

in this file, i extend the class to include three arithmetic operation: +, -, *

all functions are correct. 
please use https://www.symbolab.com/solver/polynomial-multiplication-calculator to check
"""

from q33 import Polynomial

class Polynomial_extend(Polynomial):
    """
    the function: __init__ and get_print will be used at here.
    extend to include +, -, *
    """
    
    def __check__(self, other):
        if isinstance(other, Polynomial_extend):    return other
        elif isinstance(other, str):                return Polynomial_extend(other)
        else:                                       raise ValueError("Invalid input type")


    # addition group: three functions
    def __add__(self, other):
        other = self.__check__(other)     # first check and convert the format
        result = {}                     # the resulting dic, at last self._dic = result

        # scan both self._dic and other._dic
        for power, coef in self._dic.items():
            if power in other._dic.keys():
                new_coef = coef + other._dic[power]
                if new_coef != 0:   result[power] = new_coef
            else:
                result[power] = coef
        
        # scan the remaining in the other._dic
        for power, coef in other._dic.items():
            if power not in result.keys():  result[power] = coef

        return Polynomial_extend(self._prepare_print(result))

    def __radd__(self, other):  return self + other
    
    def __iadd__(self, other):  return self + other


    # subtraction group: three functions
    def __sub__(self, other):
        other = self.__check__(other)     # first check and convert the format
        
        # subtraction, a - b is simply a + (-b)
        # make a copy for the "other"
        other_dic_copy = {}
        for power in other._dic:
            other_dic_copy[power] = -1.0 * other._dic[power]
        
        return self + Polynomial_extend(self._prepare_print(other_dic_copy))
    
    def __rsub__(self, other):  return self - other

    def __isub__(self, other):  return self - other


    # multiplication group: three functions
    def __mul__(self, other):
        """
        for multiplication: iterate "self", multiply each element in the "other".
        result stores in dic "result" and return
        """
        other = self.__check__(other)     # first check and convert the format
        result = {}

        for power1, coef1 in self._dic.items():
            for power2, coef2 in other._dic.items():
                
                # calculate the result
                new_power = power1 + power2
                new_coef = coef1 * coef2

                # add into the dic
                if new_power in result.keys():
                    result[new_power] += new_coef
                else:
                    result[new_power] = new_coef

        return Polynomial_extend(self._prepare_print(result))

    def __rmul__(self, other):  return self * other

    def __imul__(self, other): return self * other
    

"""test module"""
def test_addition():
    print("test addition\n")
    
    poly_list = [
        "5x^5+6*x^3-x-2", "x^3-2x+7",
        "-10*x^5-9*x^6-7*x^4-2x-3", "9*x^5+8*x^6+6*x^4+x+2",
        "10*x^5+9*x^6+7*x^4+2x+3", "-9*x^5-8*x^6-6*x^4-x-2"
    ]

    for i in range(3):
        print("test {}".format(i+1))
        a = Polynomial_extend(poly_list[2*i])
        b = Polynomial_extend(poly_list[2*i+1])
        c, d = a + b, b + a
        a += b
        print(str(c))
        print(str(d))
        print(str(a))
        print()
        del a, b, c, d


def test_subtraction():
    print("test subtraction\n")

    poly_list = [
        "5x^5+6*x^3-x-2", "x^3-2x+7",
        "-10*x^5-9*x^6-7*x^4-2x-3", "9*x^5+8*x^6+6*x^4+x+2",
        "10*x^5+9*x^6+7*x^4+2x+3", "-9*x^5-8*x^6-6*x^4-x-2"
    ]

    for i in range(3):
        print("test {}".format(i+1))
        a = Polynomial_extend(poly_list[2*i])
        b = Polynomial_extend(poly_list[2*i+1])
        c, d = a - b, b - a
        a -= b
        print(str(c))
        print(str(d))
        print(str(a))
        print()
        del a, b, c, d


def test_multiplication():
    
    print("test addition\n")
    
    poly_list = [
        "5x^5+6*x^3-x-2", "x^3-2x+7",
        "-10*x^5-9*x^6-7*x^4-2x-3", "9*x^5+8*x^6+6*x^4+x+2",
        "10*x^5+9*x^6+7*x^4+2x+3", "-9*x^5-8*x^6-6*x^4-x-2"
    ]

    for i in range(3):
        print("test {}".format(i+1))
        a = Polynomial_extend(poly_list[2*i])
        b = Polynomial_extend(poly_list[2*i+1])
        c, d = a * b, b * a
        a *= b
        print(str(c))
        print(str(d))
        print(str(a))
        print()
        del a, b, c, d


if __name__ == "__main__":
    # test_addition()
    # test_subtraction()
    test_multiplication()


