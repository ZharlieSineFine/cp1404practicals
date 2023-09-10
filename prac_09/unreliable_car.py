"""
CP1404/CP5632 Practical
UnreliableCar class
"""
from car import Car
from random import randint


class UnreliableCar(Car):
    """Simulate a Car class that has a unique reliability value."""

    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return the UnreliableCar info."""
        return f"{super().__str__()}, the car's reliability is {self.reliability}."

    def drive(self, distance):
        """Only drive the car if the random number is less than the car's reliability."""
        breakdown_chance = randint(0, 100)
        if breakdown_chance < self.reliability:
            super().drive(distance)
        else:
            distance = 0
        return distance
