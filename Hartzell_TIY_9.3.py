from turtledemo.clock import make_hand_shape


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

# User 1
first_user = User('christian', 'hartzell', 'Administrator', 'IT Support')
first_user.describe_user()
# Greeting User 1
greet_first_user = first_user
greet_first_user.greet_user()

# User 2
second_user = User('jack', 'palmer', 'heavily monitored user', 'chemical lab guinea pig')
second_user.describe_user()
# Greeting User 2
greet_second_user = second_user
greet_second_user.greet_user()

# User 3
third_user = User('caleb', 'york', 'user', 'electronics engineer')
third_user.describe_user()
# Greeting User 3
greet_third_user = third_user
greet_third_user.greet_user()