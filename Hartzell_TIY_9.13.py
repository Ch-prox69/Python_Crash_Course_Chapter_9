from random import randint

class Die:
    """A class for our dice"""

    def __init__(self, sides=6):
        """Create the die"""
        self.sides = sides

    def roll_die(self):
        """Rolling the die"""
        return randint(1, self.sides)

# Make the die a six sided die
dice6 = Die()

results = []
for roll_num in range(10):
    result = dice6.roll_die()
    results.append(result)
print("Here are your 10 rolls of the 6 sided dice:")
print(results)
