class Restaurant:
    """A Class on restaurants"""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant name and cuisine type"""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Tell them what our restaurant name is"""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

restaurant = Restaurant('al dente', 'american-italian')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()


