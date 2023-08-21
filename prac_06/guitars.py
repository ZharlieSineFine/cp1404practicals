"""CP1404/CP5632 Practical - Client code to use the Guitar class.
Estimate: 20 minutes
Time started: 12:19
Time finished:
"""

from cp1404practicals.prac_06.guitar import Guitar
from operator import attrgetter


def main():
    """Apply the guitar class."""
    guitars = []
    print("My guitars!")
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = input("Cost: $")
        guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
        print(f"{guitar_name} ({guitar_year}) : ${float(guitar_cost):.2f} added.")
        guitar_name = input("Name: ")

    # guitars.append(Guitar("Fender Stratocaster", 2014, 765.4))
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.sort(key=attrgetter('year'))  # Sort guitars by the year

    print("These are my guitars:")
    maximum_name_length = max(len(guitar.name) for guitar in guitars)
    maximum_cost_length = max(len(str(guitar.cost)) for guitar in guitars)
    print(maximum_cost_length)
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(
            f"Guitar {i}: {guitar.name:>{maximum_name_length}} ({guitar.year}), "
            f"worth ${guitar.cost:>10,.2f}{vintage_string}")


if __name__ == '__main__':
    main()
