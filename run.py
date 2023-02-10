# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# def ask_player_name():
#     """
#     Asks the player to input their name. A while loop runs, collecting name
#     from user which must be 15 characters or less. This loop runs continuously
#     until valid data is provided.
#     """
#     print("Hello! Welcome to Battleship\n")

#     while True:
#         name = input("Enter your name:\n")

#         if validate_input("name", name):
#             print(f"Thank you {name}, let's get ready to play!\n")
#             break

from admin import Admin
from ship import Ship
from board import Board

game = Admin([], [], [], 0, 0, 0, 0, 0)
ship_size = 3


def difficulty_choice():
    """
    Asks the player to input their difficulty choice. A while loop runs
    to collect valid string data from the user. This loop runs continuously
    until valid data is provided. The difficulty value is then returned.
    This is used to designate grid size.
    """
    print("Please Choose Difficulty")

    while True:
        difficulty = input(
            "Press E for Easy, M for Medium and H for Hard:\n").upper()

        if validate_input("difficulty", difficulty):
            if difficulty == "E":
                difficulty = "Easy"
            elif difficulty == "M":
                difficulty = "Medium"
            elif difficulty == "H":
                difficulty = "Hard"
            print(f"You've selected {difficulty}\n")
            break
    
    game.difficulty(difficulty)


def display_rules():
    print("Here are the rules:\n")

    print("Each player has 5 randomly positioned ships on the board")
    print("They will be placed horizontally or vertically\n")

    print("The 5 ships are:\n")

    print("- Carrier. Occupies 5 spaces")
    print("- Battleship. Occupies 4 spaces")
    print("- Cruiser. Occupies 3 spaces")
    print("- Submarine. Occupies 3 spaces")
    print("- Deystroyer. Occupies 2 spaces\n")

    print("Your job is to guess the position of these ships")
    print("Each player will take turns guessing coordinates")
    print("This guess will either be a 'hit' or a 'miss'")
    print("Hit all the positions taken up by a ship and you sink it")
    print("Sink all of the ships and you win!\n")

    print("Not so fast though....\n")

    print("Today you'll be playing against the old seadog Admiral M. Python")
    print("Still fancy your chances??")

    while True:
        game_start = input("Y for Yes, N for No:").upper()

        if validate_input("game_start", game_start):
            if game_start == "Y":
                print("Ok.... Let's get ready for battle!")
            elif game_start == "N":
                print("Wise decision, back to shore with you!")
            break


def validate_input(input_type, data):
    """
    Validates input from the user. Tests carried out dependant on input_type
    variable passed to function. If input is valid,True is returned and input
    passes validation. If not, False is returned and input loop continues.
    """
    
    # Name must be less than 15 characters & contain only alpha characters
    if input_type == "name":
        try:
            if len(data) > 15:
                raise ValueError("Name must be less than 15 characters\n")
            for element in data:
                if element.isalpha() is False:
                    raise ValueError("Name must only contain letters\n")
        except ValueError as e:
            print(f"Invalid name: {e}Please try again.\n")
            return False

        return True

    # Difficulty must be letter 'E', 'M' or 'H'
    if input_type == "difficulty":
        try:
            if data == "E" or data == "M" or data == "H":
                return True
            else:
                raise ValueError("Must press E, M or H\n")
        except ValueError as e:
            print(f"Invalid difficulty: {e}Please try again")
            return False

    # Game start input must be letter 'Y' or 'N'
    if input_type == "game_start":
        try:
            if data == "Y" or data == "N":
                return True
            else:
                raise ValueError("Must press Y or N\n")
        except ValueError as e:
            print(f"Invalid choice: {e}Please try again")
            return False


difficulty_choice()

ship_max = (game.ship_amount + ship_size)-1
player_score, comp_score = 0, 0

player_ships = Ship(ship_size, game.board_size, ship_max, game.ship_amount)
computer_ships = Ship(ship_size, game.board_size, ship_max, game.ship_amount)

board_1 = Board(game.board_size, "hidden")
board_2 = Board(game.board_size, "position")
board_3 = Board(game.board_size, "guess")

# def main():          
#     # ask_player_name()
    
#     # display_rules()


# main()