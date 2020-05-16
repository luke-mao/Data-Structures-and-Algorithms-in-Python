from example_sequence import Sequence

class Sequence_q22(Sequence):

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        else:
            for i in range(len(self)):
                if self[i] != other[i]: return False
            return True
            