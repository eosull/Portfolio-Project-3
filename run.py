# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from admin import Admin
from ship import Ship
from board import Board
from validation import Validation

game = Admin(0, 0, 0, 0, 0, 0)

ship_size = 3

print("Welcome to\n\n")
print("""\
            █▄▄ ▄▀█ ▀█▀ ▀█▀ █░░ █▀▀ █▀ █░█ █ █▀█
            █▄█ █▀█ ░█░ ░█░ █▄▄ ██▄ ▄█ █▀█ █ █▀▀\n\n""")

while True:
    name_input = Validation(input("Enter your name:\n"))
    if name_input.validate_name():
        print(f"Thank you {name_input.data}, let's get ready to play!")
        break

print("\n\nFirstly, Please Choose Difficulty")
while True:
    difficulty_input = Validation(input(
        "Press E for Easy, M for Medium and H for Hard:").upper())
    if difficulty_input.validate_diff():
        game.difficulty(difficulty_input.data)
        break

print("Ok, here are the rules:\n\n")

if game.ship_amount > 1:
    print(f"Each player has {game.ship_amount} ships on their board")
    print("Your job is to guess the position of the computer's ships\n\n")
else:
    print(f"Each player has {game.ship_amount} ship on their board")
    print("Your job is to guess the position of the computer's ship\n\n")

print("You & the computer will take turns guessing coordinates")
print("This guess will either be a 'hit' or a 'miss'")
print("Hit all the positions taken up by a ship and you sink it")
print("Sink all of the ships and you win!\n\n")


print("Do you want to begin?")
while True:
    start_input = Validation(input("Y for Yes, N for No:").upper())
    if start_input.validate_start():
        break

ship_max = (game.ship_amount + ship_size)-1
player_score, comp_score = 0, 0

player_ships = Ship(ship_size, game.board_size, ship_max, game.ship_amount)
computer_ships = Ship(ship_size, game.board_size, ship_max, game.ship_amount)

game.board_1 = Board(game.board_size, "hidden")
game.board_2 = Board(game.board_size, "position")
game.board_3 = Board(game.board_size, "guess")

player_ships.position_ship(1, game.board_1)
computer_ships.position_ship(2, game.board_2)

player_places, computer_places = game.count_board_places()

game.check_board_ok(player_places, computer_places,
                    player_ships, computer_ships)

print("**Your Guesses**")
game.board_3.print_board()
print("\n\n****************\n\n")

print("**Your Board**")
game.board_2.print_board()
print("\n**************\n")

print(f"Target score is {game.point_target}")
print("Good Luck!!\n")

game.guess(player_score, comp_score)
