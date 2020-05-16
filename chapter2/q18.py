from example_progression_inherit import FibonacciProgression

class FibonacciProgression_q18(FibonacciProgression):
    
    def get_n_th_number(self, n):
        if not isinstance(n, int): raise ValueError("n should be an integer")
        if not n >= 1: raise ValueError("n should be greater than 1")

        # if n = 1, then no need to advance, so n-1
        for _ in range(n-1):
            self._advance()
        
        return self._current


if __name__ == '__main__':
    f = FibonacciProgression_q18(2, 2)
    print(f.get_n_th_number(8))
    # can check using f.print_progression(8)
    # but the two sentences cannot be used together
