
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
