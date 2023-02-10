
class Board():
    """
    Class for the creation of boards used for playing Battleship
    """

    def __init__(self, size, type):
        """
        Assigns variables & calls build_board function
        """
        self.size = size
        self.type = type
        self.board = self.build_board()

    def build_board(self):
        """
        Creates lists within a list, indexing of these are
        used for x,y co-ordinates of ships eg. board[x][y]

        '~' is used for boards showing ships
        '-' used for board showing guesses
        '0' used for hidden board containing computer's ships
        """
        list = []
        for x in range(self.size):
            if self.type == "position":
                list.append(["~"] * self.size)
            elif self.type == "guess":
                list.append(["-"] * self.size)
            elif self.type == "hidden":
                list.append(["0"] * self.size)
        return list