
class Validation():
    """
    Class for validation of user input

    If input meets conditions,True is returned and input
    passes validation. If not, False is returned and input
    loop continues.
    """

    def __init__(self, data):
        self.data = data

    def validate_name(self):
        """
        Name must be less than 15 characters & contain only alpha characters
        """
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

    def validate_diff(self):
        """
        Difficulty must be letter 'E', 'M' or 'H'
        """
        try:
            if self.data == "E" or self.data == "M" or self.data == "H":
                return True
            else:
                raise ValueError("Must press E, M or H\n")
        except ValueError as e:
            print(f"Invalid difficulty: {e}Please try again")
            return False

    def validate_start(self):
        """
        Game start input must be letter 'Y' or 'N'
        """
        try:
            if self.data == "Y":
                print("Ok.... Let's get ready for battle!")
                return True
            elif self.data == "N":
                print("Wise decision, back to shore with you!")
                exit()
            else:
                raise ValueError("Must press Y or N\n")
        except ValueError as e:
            print(f"Invalid choice: {e}Please try again")
            return False
