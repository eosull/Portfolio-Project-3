
class Validation():
    """
    Class for validation of user input
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