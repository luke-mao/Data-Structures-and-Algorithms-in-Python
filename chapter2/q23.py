from example_sequence import Sequence

class Sequence_q23(Sequence):

    def __lt__(self, other):
        
        # first, at the same length, compare
        # if all equal, then the shorter length is the smallest

        for i in range(min(len(self), len(other))):
            if self[i] >= other[i]: return False

        return len(self) < len(other)
         