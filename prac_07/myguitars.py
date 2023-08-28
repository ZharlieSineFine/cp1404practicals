"""CP1404/CP5632 Practical - Client code to use the Guitar class.
Estimate: 40 minutes
Time started: 11:40
Time finished: 12:54
"""

import csv
from guitar import Guitar

NAME_INDEX = 0
YEAR_INDEX = 1
COST_INDEX = 2
FILENAME = 'guitars.csv'


def main():
    """Read all guitars and store them in a list of objects and display them after."""
    guitars = []
    in_file = open(FILENAME, 'r', newline='')
    reader = csv.reader(in_file)
    for row in reader:
        new_guitar = Guitar(row[NAME_INDEX], int(row[YEAR_INDEX]), float(row[COST_INDEX]))
        guitars.append(new_guitar)
    in_file.close()

    guitars.sort()

    for guitar in guitars:
        print(guitar)

    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
        print(f"{guitar_name} ({guitar_year}) : ${float(guitar_cost):.2f} added.")
        guitar_name = input("Name: ")

    guitars.sort()

    with open(FILENAME, "w") as out_file:
        for guitar in guitars:
            guitar_elements = [guitar.name, str(guitar.year), str(guitar.cost)]
            print(','.join(str(element) for element in guitar_elements), file=out_file)


main()
