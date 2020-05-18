"""
q33: input a general polynomial (in variable x),
     output the first order derivative, in string, in variable x

Method: design a class, accept a string of polynomial as input, then calculate the first order derivative
"""

class Polynomial:
    def __init__(self, s):
        """
        accept a string of polynomial, and translate into dictionary.
        identify the polynomial char by char, do not use regex.
        the result is a dicionary: {power: +/- coefficient}.
        
        example of input:
            x+5, -x-3, 0.00567*x^2+2*x+5, -x^7-56
        """

        self._dic = {}
        power = ""      # power is >= 0, and integer
        coef = ""       # with +/-, can be float or integer
        coef_finish = False     # both the power and coef are numbers, so need a flag to indicate the difference
                                # flag = False -> the digit you see belong to the coef

        i = 0
        while i < len(s):

            if s[i] == '+' or s[i] == '-':  # meet the sign
                if i == 0:  # if this is at the start of the polynomial
                    coef = s[i]
                
                else:       # at round middle of the polynomial
                    # before put into the dictionary, consider power is ""
                    if power == "" and coef_finish == True:     # if no power present, but has "x" present, then power = 1
                        power = "1"
                    elif power == "" and coef_finish == False:  # if no power present, and no x, then it is a constant
                        power = "0"     

                    self._dic[int(power)] = float(coef)         # finish the last part
                
                    power, coef = "", ""                        # re-initialize
                    coef_finish = False
                    coef = s[i]                                # start the next term with the sign
            
            elif s[i] == 'x' or s[i] == "*" or s[i] == "^":
                coef_finish = True
                if coef == "" or coef == "+" or coef == "-":    coef += "1"     # for +x, -x, -x^2                             
            
            elif s[i].isdigit() or s[i] == '.':                 # if the char is a digit or decimal place
                if coef_finish:
                    power += s[i]
                else:
                    coef += s[i]
            
            else:
                raise ValueError("Invalid character {}".format(s[i]))

            # at final: increment i    
            i += 1
        
        
        """
        when the iteration finish, need to deal with the last term.
        example of the last term: ......
        """

        if power == "" and coef_finish == True:     # if no power present, but has "x" present, then power = 1
            power = "1"
        elif power == "" and coef_finish == False:  # if no power present, and no x, then it is a constant
            power = "0"     

        self._dic[int(power)] = float(coef)         # finish the last part
    

    def get_print(self, dic=None):
        """
        this function is for debug only, print out the current polynomial stored in this variable.
        by default, print the polynomial stored inside the dic,
        or print the polynomial stored in the input variable "dic".
        """
        if dic is None: dic = self._dic

        # the following part will also examine whether the output is empty or not
        output = ""

        # sort power in descending order
        for power in sorted(dic, reverse=True):
            coef = dic[power]

            # coefficient
            if power == 0:
                if output == "":    output += "{}".format(coef)
                else:
                    if coef >= 0:   output += "+ {}".format(coef)
                    else:           output += "- {}".format(-coef)

            else:
                if coef < 0:
                    if output == "":
                        if coef == -1.0: output += "-"
                        else:            output += "{}".format(coef)
                    else:
                        if coef == -1.0: output += "- "
                        else:            output += "- {}".format(-coef)
                elif coef > 0:
                    if output == "":
                        if coef == 1.0:  pass
                        else:            output += "{}".format(coef)
                    else:
                        if coef == 1.0:  output += "+ "
                        else:            output += "+ {}".format(coef)

                # power
                if power == 1:
                    if output == "" or (not output[-1].isdigit()):    
                        output += "x "      # for case + x, - x, or polynomial simply start with x
                    else:                            
                        output += "*x "
                else:
                    if coef == 1.0 or coef == -1.0:
                        output += "x^{} ".format(power)
                    else:
                        output += "*x^{} ".format(power)

        print(output)


    def first_order_derivative(self):
        """
        calculate the first order derivative, and print out in the general polynomial format
        
        method:
            result is saved in a dictionary, and then print out        
        """
        derivative = {}
        for power, coef in self._dic.items():
            if power < 1: continue
            else:
                new_coef = coef * power
                new_power = power - 1
                derivative[new_power] = new_coef

        return self.get_print(derivative)


def test_polynomial_get_print():

    poly_list = [
        "x+5", 
        "2x-10",
        "5*x^3-2x-8",
        "0.99996*x^4-x^3-109x-5"
    ]
    poly_class = []

    for i in poly_list:
        poly_class.append(Polynomial(i))
        poly_class[-1].get_print()
        print()


def test_polynomial_first_order_derivative():
    
    poly_list = [
        "x+5", 
        "0.5*x^2+7",
        "2x-10",
        "5*x^3-2x-8",
        "0.99996*x^4-x^3-109x-5",
        "0.2*x^5-5x",
        "0.2*x^5+0.25*x^4+x^3+0.5*x^2+x"
    ]
    poly_class = []

    for i in poly_list:
        print(i)
        poly_class.append(Polynomial(i))
        poly_class[-1].first_order_derivative()
        print()


if __name__ == '__main__':
    test_polynomial_first_order_derivative()




        