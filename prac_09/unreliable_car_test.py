"""
CP1404/CP5632 Practical
Client code to test UnreliableCar class
"""

from unreliable_car import UnreliableCar


def main():
    new_unreliable_car = UnreliableCar(name="Buggy", fuel=120, reliability=56)
    new_unreliable_car.drive(55)
    print(new_unreliable_car)

    another_unreliable_car = UnreliableCar(name="Shady", fuel=260, reliability=78)
    another_unreliable_car.drive(89)
    print(another_unreliable_car)


main()
