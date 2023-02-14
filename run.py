# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from admin import Admin
from ship import Ship
from board import Board
from validation import Validation

game = Admin(0, 0, 0, 0, 0, 0)

ship_size = 3

print("Welcome to....")
game.load(5, 0.25)
print("""\
            █▄▄ ▄▀█ ▀█▀ ▀█▀ █   █▀▀ █▀ █ █ █ █▀█
            █▄█ █▀█  █   █  █▄▄ ██▄ ▄█ █▀█ █ █▀▀""")
game.load(5, 0.25)

while True:
    name_input = Validation(input("Enter your name:\n"))
    if name_input.validate_name():
        print(f"Thank you {name_input.data}, let's get ready to play!")
        break
game.load(2, 1)
print("Firstly, Please Choose Difficulty")
game.load(1, 1)
while True:
    difficulty_input = Validation(input(
        "Press E for Easy, M for Medium and H for Hard:").upper())
    if difficulty_input.validate_diff():
        game.difficulty(difficulty_input.data)
        break
game.load(2, 0.5)
print("Ok, here are the rules:")
game.load(1, 2)
if game.ship_amount > 1:
    print(f"Each player has {game.ship_amount} ships on their board")
    game.load(1, 2)
    print("Your job is to guess the position of the computer's ships")
    game.load(1, 2)
else:
    print(f"Each player has {game.ship_amount} ship on their board")
    game.load(1, 2)
    print("Your job is to guess the position of the computer's ship")
    game.load(1, 2)

print("You & the computer will take turns guessing coordinates")
game.load(1, 2)
print("This guess will either be a 'hit' or a 'miss'")
game.load(1, 2)
print("Hit all the positions taken up by a ship and you sink it")
game.load(1, 2)
print("Sink all of the ships and you win!")
game.load(1, 2)

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

game.print_game_status(0, 0)
print("Good Luck!!\n")

game.guess(player_score, comp_score)
