# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def ask_player_name():
    print("Hello! Welcome to Battleship")

    while True:
        name = input("Enter your name here:\n")

        if validate_input("name", name):
            print(f"Thank you {name}, let's get ready to play!")
            break


def validate_input(input_type, data):
    if input_type == "name":
        try:
            if len(data) > 15:
                raise ValueError("More than 15 characters")
        except ValueError as e:
            print(f"Invalid name: {e}, please try again.\n")
            return False

        return True


ask_player_name()