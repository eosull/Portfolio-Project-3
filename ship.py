from random import randint


class Ship():
    """
    Class to build ships for playing battleship
    """

    def __init__(self, ship_size, board_size, ship_max, ship_amount):
        """
        Assigns variables & generates safe_zone variable for
        placement of ships without going off board
        """
        self.ship_size = ship_size
        self.board_size = board_size
        self.ship_max = ship_max
        self.ship_amount = ship_amount
        self.safe_zone = board_size - ship_max

    def position(self):
        """
        Generates and returns random row and column position
        """
        row_start = randint(0, self.safe_zone)
        column_start = randint(0, self.safe_zone)
        return row_start, column_start

    def position_ship(self, player, board):
        """
        Checks generated positions against the populated
        board to prevent duplication
        """
        for ship_increase in range(0, self.ship_amount):
            row, column = self.position()
            for row_check in range(0, self.ship_size + ship_increase):
                for column_check in range(0, self.ship_size + ship_increase):
                    check_pos = board.board[row + row_check][
                        column + column_check]
                    while (check_pos == "1") or (check_pos == "±"):
                        row, column = self.position()
                        check_pos = board.board[row + row_check][
                            column + column_check]
            self.place_ship(row, column, ship_increase, player, board)

    def place_ship(self, row, column, ship_increase, player, board):
        """
        Marks the board where ships to be positioned
        Random num generated to decide whether horizontal
        or vertical
        """
        direction = randint(0, 1)
        for i in range(0, self.ship_size + ship_increase):
            if player == 1:
                if direction == 0:
                    board.board[row + i][column] = str(player)
                elif direction == 1:
                    board.board[row][column + i] = str(player)
            elif player == 2:
                if direction == 0:
                    board.board[row + i][column] = "±"
                elif direction == 1:
                    board.board[row][column + i] = "±"
