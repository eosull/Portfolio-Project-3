
import time
from random import randint
from validation import Validation
from rich import print


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
        Boards are cleared and re-populated if correct amount
        of places are not taken up by ships
        """
        while (player_places != self.point_target) or (computer_places !=
                                                       self.point_target):
            self.board_1.clear_board(1)
            self.board_2.clear_board(2)

            player_ships.position_ship(1, self.board_1)
            computer_ships.position_ship(2, self.board_2)

            player_places, computer_places = self.count_board_places()

    def count_board_places(self):
        """
        Counts the amount of places on each board taken up by
        ships
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
            print("\nYou've chosen Easy")
        elif choice == "M":
            self.board_size = 6
            self.ship_amount = 2
            self.point_target = 7
            print("\nYou've chosen Medium")
        elif choice == "H":
            self.board_size = 8
            self.ship_amount = 3
            self.point_target = 12
            print("\nYou've chosen Hard")

    def guess(self, player_score, comp_score):
        """
        Validates user guess input and generates computer guess
        These guesses are checked using check_guess function
        Game status is printed and scores are checked for win
        """
        while (player_score < self.point_target) and (comp_score
                                                      < self.point_target):
            # Player Guess
            while True:
                guess_row = Validation(input(
                            f"Choose Row 0-{self.board_size-1}:\n"))
                if guess_row.validate_guess(self.board_size-1):
                    row_val = int(guess_row.data)
                    break
            while True:
                guess_column = Validation(input(
                            f"Choose column 0-{self.board_size-1}:\n"))
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

            self.print_game_status(player_score, comp_score)
            self.check_if_win(player_score, comp_score)

    def check_guess(self, board, guess_board, row, column, player, score):
        """
        Asks for another input if guess has already been made by user
        Generates another random guess for computer if guess already been made
        Score incremented if hit, returned unchanged if miss
        """
        if player == 1:
            previous_guess = guess_board.board[row][column]
            while (previous_guess == "o") or (previous_guess == "X"):
                print("You've already guessed here!")
                print("Guess Again!!")
                row = int(input(f"Choose Row 0-{self.board_size-1}:\n"))
                column = int(input(f"Choose Column 0-{self.board_size-1}:\n"))
                previous_guess = board.board[row][column]

        guess = board.board[row][column]
        while (guess == "o") or (guess == "X"):
            row = randint(0, self.board_size-1)
            column = randint(0, self.board_size-1)
            guess = board.board[row][column]

        if guess == "0" or guess == "~":
            if player == 1:
                self.load(1, 0.5)
                print("You missed!!")
                guess_board.board[row][column] = "o"
            if player == 2:
                self.load(1, 0.25)
                print("Computer missed!!")
                board.board[row][column] = "o"
            return score

        elif (guess == "1") or (guess == "±"):
            if player == 1:
                self.load(1, 0.5)
                print("You hit a ship!!")
                guess_board.board[row][column] = "X"
            elif player == 2:
                self.load(1, 0.5)
                print("Computer hit a ship!!")
                board.board[row][column] = "X"
            score += 1
            return score

    def print_game_status(self, player_score, comp_score):
        """
        Prints out game status after each validated guess
        Includes boards, key for boards and scores
        """
        self.load(1, 0.125)
        print("********************************")
        self.load(1, 0.125)
        print("             [dark_orange]Your Guesses[dark_orange]", end="      ")

        print(f"Your score: {player_score}")
        self.load(1, 0.125)
        self.board_3.print_board()
        self.load(1, 0.125)
        print("             [dark_orange]Your Board[/dark_orange]", end="       ")
        print(f"Computer score is {comp_score}")
        self.load(1, 0.125)
        self.board_2.print_board()
        self.load(1, 0.125)
        print("********************************")
        print(f"Score {self.point_target} to win")

    def check_if_win(self, player_score, comp_score):
        """
        Checks if computer or player have met the target score
        """
        if player_score == self.point_target:
            print("You Win!!!\n")
            print("Congrats!!")
        elif comp_score == self.point_target:
            print("You Lose!!")
            print("Unlucky!")

    def load(self, lines, time_per_line):
        """
        Simulates loading by printing character followed by sleep
        """
        for _ in range(0, lines):
            print(" ")
            time.sleep(time_per_line)
