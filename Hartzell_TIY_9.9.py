class Car:
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=60):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range of the battery."""
        if self.battery_size == 50:
            range_value = 120
        elif self.battery_size == 65:
            range_value = 165
        else:
            range_value = 240  # Assume a default for other sizes

        message = f"This car can go approximately {range_value} miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """Upgrade the battery."""
        if self.battery_size < 85:  # Assuming 85 is the highest option
            self.battery_size = 85
            print("Upgraded the battery to 85 kWh.")
        else:
            print("The battery is already upgraded.")


class ElectricCar(Car):
    """Models aspects of an electric car."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


# Testing the implementation
print("Make an electric car, and describe the battery:")
my_prius = ElectricCar('Toyota', 'Prius', 2023)
my_prius.battery.describe_battery()

print("\nUpgrade the battery, and check the battery again:")
my_prius.battery.upgrade_battery()
my_prius.battery.describe_battery()

print("\nTry upgrading the battery a second time.")
my_prius.battery.upgrade_battery()
my_prius.battery.describe_battery()
