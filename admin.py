
from random import randint


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

    def difficulty(choice):
        """
        Takes user difficulty input and sets game
        settings to be used for game setup        
        """
        if choice == "E":
            board_size = 4
            ship_amount = 1
            point_target = 3
        elif choice == "M":
            board_size = 6
            ship_amount = 2
            point_target = 7
        elif choice == "H":
            board_size = 8
            ship_amount = 3
            point_target = 12
        return board_size, ship_amount, point_target

def guess(self, player_score, player_target, comp_score,
    computer_target, board_1, board_2, board_3, board_size):
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
        while (player_score < player_target) and (comp_score < computer_target):

            guess_row = int(input(f"Choose Row 0-{board_size-1}:"))
            guess_column = int(input(f"Choose column 0-{board_size-1}:"))
            player_score = self.check_guess(board_1, board_3, guess_row,
            guess_column, 1, board_size, player_score)

            guess_comp_row = randint(0,board_size-1)
            guess_comp_column = randint(0,board_size-1)
            comp_score = self.check_guess(board_2, board_3, guess_comp_row,
            guess_comp_column, 2, board_size, comp_score)

            print("\n********************************\n")
            print("**Your Guesses**\n")
            board_3.print_board()
            print("\n********\n")
            
            print("\n**Your board**\n")
            board_2.print_board()
            print("\n********\n")

            print("~ = Water")
            print("± = Ship")
            print("X = Hit")
            print("o = Miss\n")

            print(f"Your score: {player_score}")
            print(f"Computer score is {comp_score}\n")
            print(f"Score {player_target} to win\n")

            self.check_if_win(player_score, comp_score, player_target, computer_target)


def check_guess(board, guess_board, row, column, player, board_size, score):
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
            row = int(input(f"Choose Row 0-{board_size-1}:"))
            column = int(input(f"Choose Column 0-{board_size-1}:"))
            previous_guess = board.board[row][column]

    guess = board.board[row][column]
    while (guess == "o") or (guess == "X"):
        row = randint(0, board_size-1)
        column = randint(0, board_size-1)
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


def check_if_win(player_score, comp_score, player_target, computer_target):
    """
    checks to see if computer or player have met the target score
    if either have, user informed whether win or loss
    """
    if player_score == player_target:
        print("You Win!!!\n")
        print("Congrats!!")
    elif comp_score == computer_target:
        print("You Lose!!")
        print("Unlucky!")
