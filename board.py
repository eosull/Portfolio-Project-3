
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

    def print_board(self):
        """
        Prints items in list in grid formation 
        Builds concantenated topline string as guide for top
        of board

        Similar guide added to start of each line using iteration
        through board size combined with .join() to add a space
        between all items in list 
        """
        topline = "   "
        for i in range(self.size):
            topline += (" " + str(i))
        print(f"{topline}\n")
        number = 0
        for row in self.board:
            print(number, " ", (" ").join(row))
            number += 1

    def clear_board(self, player):
        """
        clear_board sets board back to empty in case of overlapping
        ships
        """
        self.board.clear()
        self.board = []
        if player == 1:
            print("Board 1 Cleared")
            for x in range(self.size):
                self.board.append(["0"] * self.size)
        if player == 2:
            print("Board 2 Cleared")
            for y in range(self.size):
                self.board.append(["~"] * self.size)  
