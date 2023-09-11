"""
CP1404/CP5632 Practical
Client code to test Taxi and SilverServiceTaxi class
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
VALID_OPTIONS = ('q', 'c', 'd')


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill_to_date = 0.0
    print("Let's drive!")
    print(MENU)
    user_option = input(">>> ").lower()
    while user_option != 'q':
        if user_option == 'c':
            print("Taxis available:")
            number_to_taxi = display_taxis(taxis)
            number_choice = int(input("Choose taxi: "))
            if number_choice not in number_to_taxi.keys():
                print("Invalid taxi choice.")
            else:
                current_taxi = number_to_taxi[number_choice]
        elif user_option == 'd':
            if current_taxi:
                drive_distance = int(input("Drive how far? "))
                current_taxi.start_fare()
                current_taxi.drive(drive_distance)
                print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")
                bill_to_date += current_taxi.get_fare()
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option.")
        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        user_option = input(">>> ").lower()
    print(f"Total trip cost: ${bill_to_date:.2f}")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display the taxis with assigned number."""
    number_to_taxi = {i: taxi for i, taxi in enumerate(taxis, 0)}
    for i in number_to_taxi.keys():
        print(f"{i} - {number_to_taxi[i]}")
    return number_to_taxi


if __name__ == '__main__':
    main()
