
class Admin():
    """
    Class to perform admin such:
    * Setting target scores
    * Checking guesses
    * Making sure ships are not overlapping
    * Checking for a win
    """

    def check_board_ok(self, player_places, computer_places, point_target,
                       board_1, board_2, player_ships, computer_ships,
                       board_size):
        """
        Used to test if correct amount of ships are on the board

        Tests places taken up on each board against the point
        target which is the sum of all ship sizes

        If they don't match, boards are cleared and re-populated

        This repeats until places taken up on board matches point
        target
        """
        while (player_places != point_target) or (computer_places != point_target):
            board_1.clear_board(1)
            board_2.clear_board(2)

            player_ships.position_ship(1,board_1)
            computer_ships.position_ship(2,board_2)
