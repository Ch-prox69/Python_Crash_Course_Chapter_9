"""A collection of classes for modeling an admin user account."""

from user import User

class Admin(User):
    """A class for the Admin"""

    def __init__(self, first_name, last_name, level_of_access, role):
        """Initialize our admin"""
        super().__init__(first_name, last_name, level_of_access, role)

        # Initialize empty privilege list
        self.privileges = Privileges()

class Privileges:
    """A class to store Admin privileges"""

    def __init__(self, privileges=None):
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("User has no privileges.")