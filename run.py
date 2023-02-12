# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# def ask_player_name():
#     """
#     Asks the player to input their name. A while loop runs, collecting name
#     from user which must be 15 characters or less. This loop runs until
#     valid data is provided.
#     """
#     print("Hello! Welcome to Battleship\n")

from admin import Admin
from ship import Ship
from board import Board
from validation import Validation

game = Admin(0, 0, 0, 0, 0, 0)

ship_size = 3

while True:
    name_input = Validation(input("Enter your name:\n"))
    if name_input.validate_name():
        print(f"Thank you {name_input.data}, let's get ready to play!\n")
        break


print("Please Choose Difficulty")
while True:
    difficulty_input = Validation(input(
        "Press E for Easy, M for Medium and H for Hard:\n").upper())
    if difficulty_input.validate_diff():
        game.difficulty(difficulty_input.data)
        break


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


ship_max = (game.ship_amount + ship_size)-1
player_score, comp_score = 0, 0

player_ships = Ship(ship_size, game.board_size, ship_max, game.ship_amount)
computer_ships = Ship(ship_size, game.board_size, ship_max, game.ship_amount)

game.board_1 = Board(game.board_size, "hidden")
game.board_2 = Board(game.board_size, "position")
game.board_3 = Board(game.board_size, "guess")

player_ships.position_ship(1, game.board_1)
computer_ships.position_ship(2, game.board_2)

player_places, computer_places = game.set_target_score()

game.check_board_ok(player_places, computer_places,
                    player_ships, computer_ships)

print("\n**Your Guesses**\n")
game.board_3.print_board()
print("\n****************\n")

print("\n**Your Board**\n")
game.board_2.print_board()
print("\n**************\n")

print(f"Target score is {game.point_target}")
print("Good Luck!!\n")

game.guess(player_score, comp_score)