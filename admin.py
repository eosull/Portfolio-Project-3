
class Admin():
    """
    Class to perform admin such:
    * Setting target scores
    * Checking guesses
    * Making sure ships are not overlapping
    * Checking for a win
    """

    def check_board_ok(player_places, computer_places, point_target,
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

            player_ships.position_ship(1, board_1)
            computer_ships.position_ship(2, board_2)

            player_places, computer_places = Admin.set_target_score(board_size, board_1, board_2)


    def set_target_score(board_size, board_1, board_2):
        """
        Used to set target score for player and computer

        Also used to verify both boards contain the right
        amount of ships

        All items on each board are tested and amount of
        positions with ships are calculated
        """
        player_target, computer_target = 0, 0
        for i in range(board_size):
            for j in range(board_size):
                if board_1.board[i][j] == "1":
                    player_target += 1
                if board_2.board[i][j] == "±":
                    computer_target += 1
        return player_target, computer_target
