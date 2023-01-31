# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def ask_player_name():
    print("Hello! Welcome to Battleship")
    name = input("Enter your name here:\n")

    print(f"Thank you {name}, let's get ready to play!")


ask_player_name()