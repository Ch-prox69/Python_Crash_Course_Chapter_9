class Restaurant:
    """A Class on restaurants"""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant name and cuisine type"""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Tell them what our restaurant name is"""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served"""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served

restaurant = Restaurant('al dente', 'american-italian')
restaurant.describe_restaurant()

print("\nNumber of people served: " + str(restaurant.number_served))
restaurant.number_served = 50
print("Number of people served: " + str(restaurant.number_served))

restaurant.set_number_served(2000)
print("Number of people served " + str(restaurant.number_served))

restaurant.increment_number_served(5000)
print("Number of people served: " + str(restaurant.number_served))