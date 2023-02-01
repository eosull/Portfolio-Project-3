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
            print(f"Thank you {name}, let's get ready to play!\n")
            break


def difficulty_choice():
    """
    Asks the player to input their difficulty choice. A while loop runs
    to collect valid string data from the user. This loop runs continuously
    until valid data is provided. The difficulty value is then returned.
    This is used to designate grid size.
    """
    print("Please Choose Difficulty")

    while True:
        difficulty = input("Press E for Easy, M for Medium and H for Hard:\n").upper()

        if validate_input("difficulty", difficulty):
            if difficulty == "E":
                difficulty = "Easy"
            elif difficulty == "M":
                difficulty = "Medium"
            elif difficulty == "H":
                difficulty = "Hard"
            print(f"You've selected {difficulty}")
            break

    return difficulty    


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
        
            
ask_player_name()
difficulty_choice()