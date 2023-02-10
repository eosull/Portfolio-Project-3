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
        Calls position function for each ship required

        The returned positions are tested to make sure
        they are not already take by a ship

        If they are new position is generated and tested

        Once this is passed place_ship function called to
        place the ship onto the required board
        """
        for j in range(0, self.ship_amount):
            x, y = self.position()
            for row_check in range(0, self.ship_size + j):
                for column_check in range(0, self.ship_size + j):
                    check_pos = board.board[x+row_check][y+column_check]
                    while (check_pos == "1") or (check_pos == "±"):
                        x, y = self.position()
                        check_pos = board.board[x+row_check][y+column_check]
            self.place_ship(x, y, j, player, board)

    def place_ship(self, x, y, j, player, board):
        """
        Generates random number to decide whether ship
        will be horizontal or vertical

        Using ship_size variable (increases on each ship)
        ship is built out from starting point, placing
        either a '1' or a '±' to mark position
        """
        direction = randint(0, 1)
        for i in range(0, self.ship_size + j):
            if player == 1:
                if direction == 0:
                    board.board[x + i][y] = str(player)
                elif direction == 1:
                    board.board[x][y + i] = str(player)
            elif player == 2:
                if direction == 0:
                    board.board[x + i][y] = "±"
                elif direction == 1:
                    board.board[x][y + i] = "±"
