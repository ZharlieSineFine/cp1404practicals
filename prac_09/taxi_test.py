"""
CP1404/CP5632 Practical
Taxi class
"""
# from car import Car
from taxi import Taxi


def main():
    new_taxi = Taxi(name="Prius 1", fuel=100)
    new_taxi.start_fare()
    new_taxi.drive(40)
    print(f"{new_taxi}, and the fare is ${new_taxi.get_fare()}")
    new_taxi.start_fare()
    new_taxi.drive(100)
    print(f"{new_taxi}, and the fare is ${new_taxi.get_fare()}")


main()
