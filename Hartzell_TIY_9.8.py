class User:
    """A simple class on User"""

    def __init__(self, first_name, last_name, level_of_access, role):
        """Start the attribute describing them"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.level_of_access = level_of_access.title()
        self.role = role.title()

    def describe_user(self):
        """Tell what the first name is"""
        msg = f"The user's first name is {self.first_name} and the user's last name is {self.last_name}."
        print(f"\n{msg}")

        msg = f"The user's level of access is {self.level_of_access}."
        print(f"\n{msg}")

        msg = f"The user's role is {self.role}."
        print(f"\n{msg}")

    def greet_user(self):
        """Greet the user"""
        msg = f"Hello {self.first_name} {self.last_name}, welcome to Python."
        print(f"\n{msg}")


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


# Creating an admin instance
christian = Admin('christian', 'hartzell', 'Admin', 'System Administrator')
christian.describe_user()

# Show current privileges (which will be empty)
christian.privileges.show_privileges()

# Define user privileges
print("\nAdding privileges")
christian.privileges.privileges = [
    'can delete posts',
    'can ban user',
    'can create user',
]
# Show updated privileges
christian.privileges.show_privileges()
