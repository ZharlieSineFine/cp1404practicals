"""CP1404/CP5632 Practical - Client code to use the Guitar class.
Estimate: 20 minutes
Time started: 11:25
Time finished: 11:38
"""

import csv
from guitar import Guitar

NAME_INDEX = 0
YEAR_INDEX = 1
COST_INDEX = 2


def main():
    """Read all guitars and store them in a list of objects and display them after."""
    guitars = []
    in_file = open('guitars.csv', 'r', newline='')
    reader = csv.reader(in_file)
    for row in reader:
        new_guitar = Guitar(row[NAME_INDEX], row[YEAR_INDEX], float(row[COST_INDEX]))
        guitars.append(new_guitar)
    in_file.close()

    for guitar in guitars:
        print(guitar)


main()
