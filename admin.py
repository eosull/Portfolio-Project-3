
from random import randint
from validation import Validation


class Admin():
    """
    Class to perform admin such:
    * Setting target scores
    * Checking guesses
    * Making sure ships are not overlapping
    * Checking for a win
    """
    def __init__(self, board_1, board_2, board_3, board_size,
                 ship_amount, point_target):
        self.board_1 = board_1
        self.board_2 = board_2
        self.board_3 = board_3
        self.board_size = board_size
        self.ship_amount = ship_amount
        self.point_target = point_target

    def check_board_ok(self, player_places, computer_places,
                       player_ships, computer_ships):
        """
        Used to test if correct amount of ships are on the board

        Tests places taken up on each board against the point
        target which is the sum of all ship sizes

        If they don't match, boards are cleared and re-populated

        This repeats until places taken up on board matches point
        target
        """
        while (player_places != self.point_target) or (computer_places !=
                                                       self.point_target):
            self.board_1.clear_board(1)
            self.board_2.clear_board(2)

            player_ships.position_ship(1, self.board_1)
            computer_ships.position_ship(2, self.board_2)

            player_places, computer_places = self.set_target_score()

    def set_target_score(self):
        """
        Used to set target score for player and computer

        Also used to verify both boards contain the right
        amount of ships

        All items on each board are tested and amount of
        positions with ships are calculated
        """
        player_target, computer_target = 0, 0
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board_1.board[i][j] == "1":
                    player_target += 1
                if self.board_2.board[i][j] == "±":
                    computer_target += 1
        return player_target, computer_target

    def difficulty(self, choice):
        """
        Takes user difficulty input and sets game
        settings to be used for game setup
        """
        if choice == "E":
            self.board_size = 4
            self.ship_amount = 1
            self.point_target = 3
            print("You've chosen Easy")
        elif choice == "M":
            self.board_size = 6
            self.ship_amount = 2
            self.point_target = 7
            print("You've chosen Medium")
        elif choice == "H":
            self.board_size = 8
            self.ship_amount = 3
            self.point_target = 12
            print("You've chosen Hard")

    def guess(self, player_score, comp_score):
        """
        Takes user guess via input function and sends this input
        to check_guess function to check if it has been guessed
        already and whether it is a hit or miss

        Random guess then generated for computer guess and process
        is repeated

        Boards, symbol key and scores are then printed out

        This process is repeated by using until while loop
        is broken, at which point either player or computer is
        declared the winner

        These conditions are tested using check_if_win function
        """
        while (player_score < self.point_target) and (comp_score
                                                      < self.point_target):
            # Player Guess
            while True:
                guess_row = Validation(input(
                            f"Choose Row 0-{self.board_size-1}:"))
                if guess_row.validate_guess(self.board_size-1):
                    row_val = int(guess_row.data)
                    break
            while True:
                guess_column = Validation(input(
                            f"Choose column 0-{self.board_size-1}:"))
                if guess_column.validate_guess(self.board_size-1):
                    col_val = int(guess_column.data)
                    break
            player_score = self.check_guess(self.board_1, self.board_3,
                                            row_val, col_val, 1, player_score)

            # Computer Guess
            guess_comp_row = randint(0, self.board_size-1)
            guess_comp_column = randint(0, self.board_size-1)
            comp_score = self.check_guess(self.board_2, self.board_3,
                                          guess_comp_row, guess_comp_column,
                                          2, comp_score)

            print("\n********************************\n")
            print("**Your Guesses**\n")
            self.board_3.print_board()
            print("\n********\n")

            print("\n**Your board**\n")
            self.board_2.print_board()
            print("\n********\n")

            print("~ = Water")
            print("± = Ship")
            print("X = Hit")
            print("o = Miss\n")

            print(f"Your score: {player_score}")
            print(f"Computer score is {comp_score}\n")
            print(f"Score {self.point_target} to win\n")

            self.check_if_win(player_score, comp_score)

    def check_guess(self, board, guess_board, row, column, player, score):
        """
        For player, guess board is first tested to see if
        guess has already been made. for computer, board with
        player's ships is tested for same

        If it has already been guessed then new guess generated
        by either asking for further user input or generating
        another random guess. this process is repeated until
        original guess is received

        When guess passes this stage, board is tested to see
        if it is a 'hit' or a 'miss'

        For hit or miss, 'X' or '0' (respectively) is placed on
        either player's guess board or board with player's ships

        Score is incremented if either make a hit. score then
        returned to be tested for winner
        """
        if (player == 1):
            previous_guess = guess_board.board[row][column]
            while (previous_guess == "o") or (previous_guess == "X"):
                print("You've already guessed here!")
                print("Guess Again!!")
                row = int(input(f"Choose Row 0-{self.board_size-1}:"))
                column = int(input(f"Choose Column 0-{self.board_size-1}:"))
                previous_guess = board.board[row][column]

        guess = board.board[row][column]
        while (guess == "o") or (guess == "X"):
            row = randint(0, self.board_size-1)
            column = randint(0, self.board_size-1)
            guess = board.board[row][column]

        if guess == "0" or guess == "~":
            if player == 1:
                guess_board.board[row][column] = "o"
            if player == 2:
                board.board[row][column] = "o"
            return score

        elif (guess == "1") or (guess == "±"):
            if player == 1:
                guess_board.board[row][column] = "X"
            elif player == 2:
                board.board[row][column] = "X"
            score += 1
            return score

    def check_if_win(self, player_score, comp_score):
        """
        checks to see if computer or player have met the target score
        if either have, user informed whether win or loss
        """
        if player_score == self.point_target:
            print("You Win!!!\n")
            print("Congrats!!")
        elif comp_score == self.point_target:
            print("You Lose!!")
            print("Unlucky!")
