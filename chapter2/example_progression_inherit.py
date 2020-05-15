from example_progression import Progression

class ArithmeticProgression(Progression):
    """arithmetic progression, inherit the class Progression"""

    def __init__(self, start=0, increment=1):
        super().__init__(start=start)
        self._increment = increment
    
    def _advance(self):
        self._current += self._increment


class GeometricProgression(Progression):
    """geometric progression"""

    def __init__(self, start=1, ratio=2):
        super().__init__(start=start)
        self._ratio = ratio
    
    def _advance(self):
        self._current *= self._ratio


class FibonacciProgression(Progression):
    """fibonacci progression"""

    def __init__(self, first=0, second=1):
        super().__init__(start=first)
        self._current = first
        self._after = second
    
    def _advance(self):
        self._current, self._after = self._after, self._current + self._after
    

if __name__ == '__main__':
    ArithmeticProgression(1, 2).print_progression(10)
    GeometricProgression().print_progression(10)
    FibonacciProgression(4, 6).print_progression(10)