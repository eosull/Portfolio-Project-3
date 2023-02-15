from rich.console import Console
from admin import Admin
from ship import Ship
from board import Board
from validation import Validation

# Create instance of game and rich console
game = Admin(0, 0, 0, 0, 0, 0)
console = Console()

# Default ship size declaration
SHIP_SIZE = 3

# Printing out game logo
game.load(5, 0.125)
console.print("""[bold dark_orange]\
            █▄▄ ▄▀█ ▀█▀ ▀█▀ █   █▀▀ █▀ █ █ █ █▀█
            █▄█ █▀█  █   █  █▄▄ ██▄ ▄█ █▀█ █ █▀▀[/bold dark_orange]""")
game.load(5, 0.125)

# Take user name input and validate
while True:
    name_input = Validation(input("Hello, please enter your name:\n"))
    if name_input.validate_name():
        print(f"Thank you {name_input.data}, let's get ready to play!")
        break
game.load(2, 0.25)

# Take user difficulty input and verify
console.print("[dark_orange]Please Choose Difficulty[/dark_orange]")
while True:
    difficulty_input = Validation(input(
        "Press E for Easy, M for Medium and H for Hard:\n").upper())
    if difficulty_input.validate_diff():
        game.difficulty(difficulty_input.data)
        break
game.load(2, 0.5)

# Print out game rules
print("Here are the rules:")
game.load(1, 1)
if game.ship_amount > 1:
    print(f"Each player has {game.ship_amount} ships on their board")
    game.load(1, 0.25)
    print("Your job is to guess the position of the computer's ships")
    game.load(1, 0.25)
else:
    print(f"Each player has {game.ship_amount} ship on their board")
    game.load(1, 0.25)
    print("Your job is to guess the position of the computer's ship")
    game.load(1, 0.25)
print(f"Score {game.point_target} to win")
game.load(1, 0.25)
print("You & the computer will take turns guessing coordinates")
game.load(1, 0.25)
print("This guess will either be a 'hit' or a 'miss'")
game.load(1, 0.25)
print("Hit all the positions taken up by a ship and you sink it")
game.load(1, 0.25)
print("Sink all of the ships and you win!")
game.load(1, 0.25)
print("~ = Water")
print("± = Ship")
print("X = Hit")
print("o = Miss")
game.load(1, 0.125)

# Ask player to confirm start and verify input
console.print("[dark_orange]Do you want to begin?[/dark_orange]")
while True:
    start_input = Validation(input("Y for Yes, N for No:").upper())
    if start_input.validate_start():
        break

# Assign ship max size and score variables
ship_max = (game.ship_amount + SHIP_SIZE) - 1
player_score, comp_score = 0, 0

# Create 3 boards to play the game
game.board_1 = Board(game.board_size, "hidden")
game.board_2 = Board(game.board_size, "position")
game.board_3 = Board(game.board_size, "guess")

# Create and position ships on board 1 & 2
player_ships = Ship(SHIP_SIZE, game.board_size, ship_max, game.ship_amount)
computer_ships = Ship(SHIP_SIZE, game.board_size, ship_max, game.ship_amount)
player_ships.position_ship(1, game.board_1)
computer_ships.position_ship(2, game.board_2)

# Count amount of places taken by ships and verify if game can start
player_places, computer_places = game.count_board_places()
game.check_board_ok(player_places, computer_places,
                    player_ships, computer_ships)

# Print out boards and scores
game.print_game_status(0, 0)

# Ask player for guess and run game
game.guess(player_score, comp_score)
