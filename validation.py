
class Validation():
    """
    Class for validation of user input
    Validates input from the user. Tests carried out dependant on input_type
    variable passed to function. If input is valid,True is returned and input
    passes validation. If not, False is returned and input loop continues.
    """

    def __init__(self, data):
        self.data = data

    # Name must be less than 15 characters & contain only alpha characters
    def validate_name(self):
        try:
            if len(self.data) > 15:
                raise ValueError("Name must be less than 15 characters\n")
            for element in self.data:
                if element.isalpha() is False:
                    raise ValueError("Name must only contain letters\n")
        except ValueError as e:
            print(f"Invalid name: {e}Please try again.\n")
            return False

        return True

    # Difficulty must be letter 'E', 'M' or 'H'
    def validate_diff(self):
        try:
            if self.data == "E" or self.data == "M" or self.data == "H":
                return True
            else:
                raise ValueError("Must press E, M or H\n")
        except ValueError as e:
            print(f"Invalid difficulty: {e}Please try again")
            return False

    # Game start input must be letter 'Y' or 'N'
    def validate_start(self):
        try:
            if self.data == "Y":
                print("Ok.... Let's get ready for battle!")
                return True
            elif self.data == "N":
                print("Wise decision, back to shore with you!")
                return True
            else:
                raise ValueError("Must press Y or N\n")
        except ValueError as e:
            print(f"Invalid choice: {e}Please try again")
            return False