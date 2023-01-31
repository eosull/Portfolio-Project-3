# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def ask_player_name():
    """
    Asks the player to input their name. A while loop runs, collecting name
    from user which must be 15 characters or less. This loop runs continuously
    until valid data is provided.
    """
    print("Hello! Welcome to Battleship\n")

    while True:
        name = input("Enter your name:\n")

        if validate_input("name", name):
            print(f"Thank you {name}, let's get ready to play!")
            break


def validate_input(input_type, data):
    """
    Validates input from the user. Tests carried out dependant on input_type
    variable passed to function. Name input is required to be less than 15
    characters and contain only alphabetical characters. If input is valid,
    True is returned and input passes validation. If not, False is returned
    and input loop continues.
    """
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


ask_player_name()