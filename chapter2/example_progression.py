class Progression:
    """
    iterator producing a generic progression
    default: 0, 1, 2, ..... to infinity
    """

    def __init__(self, start=0):
        self._current = start
    
    def _advance(self):
        self._current += 1
    
    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer
    
    def __iter__(self):
        return self
    
    def print_progression(self, n):
        if not n >= 1:
            raise ValueError("Print times must >= 0")
        print(' '.join([str(next(self)) for i in range(n)]))


if __name__ == '__main__':
    Progression().print_progression(10)