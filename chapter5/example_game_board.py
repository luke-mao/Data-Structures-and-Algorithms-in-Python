class GameEntry:
    """represent one entry of a list of high scores"""

    def __init__(self, name, score):
        self._name = name
        self._score = score
    
    def get_name(self):     return self._name

    def get_score(self):    return self._score

    def __str__(self):
        return "{}, {}".format(self._name, self._score)


def test_GameEntry():
    a = GameEntry("John", 100)
    print(a.get_name(), a.get_score())

    b = GameEntry("Ann", 200)
    print(b.get_name(), b.get_score())


class Scoreboard:
    """score board: contain top n entries of the game score"""

    def __init__(self, capacity=10):
        self._board = [None] * capacity     # initialize to the max size
        self._n = 0      # record numbers of scores in the array
        self._capacity = capacity

    def __getitem__(self, k):
        return self._board[k]
    
    def __str__(self):
        return "\n".join(str(self._board[k]) for k in range(self._n))
    
    def add(self, entry):
        # the entry belongs to the class GameEntry

        # first check if the board is full or not

        if self._n < self._capacity or entry.get_score() > self._board[-1].get_score():
            """
            only when the score has available slots, or the score is higher than at least one on the board,
            then the insertion can work
            """

            if self._n < self._capacity: self._n += 1

            i = self._n -1

            # note: self_board[i-1] !!!
            # entry score is definitely > self._board[i] score, where i = n-1
            # so compare the entry score and [i-1] score !!!
            while i > 0 and entry.get_score() > self._board[i-1].get_score():
                self._board[i] = self._board[i-1]
                i -= 1
            
            self._board[i] = entry





def test_Scoreboard():
    
    s = Scoreboard(4)
    
    entry_list = [
        GameEntry("A", 400),
        GameEntry("B", 500),
        GameEntry("C", 600),
        GameEntry("D", 700),
        GameEntry("E", 800),
        GameEntry("F", 900),
        GameEntry("G", 1000),
        GameEntry("H", 1100)
    ]

    for entry in entry_list:
        s.add(entry)
        print(str(s))
        print()


if __name__ == '__main__':
    # test_GameEntry()
    test_Scoreboard()