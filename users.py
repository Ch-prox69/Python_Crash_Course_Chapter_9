class User:
    """A simple class on User"""

    def __init__(self, first_name, last_name, level_of_access, role):
        """Start the attribute describing them"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.level_of_access = level_of_access.title()
        self.role = role.title()
        self.login_attempts = 0

    def describe_user(self):
        """Tell what the first name is"""
        msg = f"The user's first name is {self.first_name} and the users last name is {self.last_name}"
        print(f"\n{msg}")

        msg = f"The user's LOA is {self.level_of_access}"
        print(f"\n{msg}")

        msg = f"The user's role is {self.role}"
        print(f"\n{msg}")

    def greet_user(self):
        """Greet the user"""
        msg = f"Hello {self.first_name} {self.last_name}, welcome to Python"
        print(f"\n{msg}")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to 0"""
        self.login_attempts = 0