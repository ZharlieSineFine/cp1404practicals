"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    totals = calculate_totals(incomes)
    print_report(incomes, totals)


def calculate_totals(incomes):
    """Calculate the totals."""
    totals = []
    total = 0
    for income in incomes:
        total += income
        totals.append(total)
    return totals


def print_report(incomes, totals):
    """Print the income report."""
    print("\nIncome Report\n-------------")
    for i in range(len(incomes)):
        print(f"Month {i + 1:>2} - Income: ${incomes[i]:>10.2f} Total: ${totals[i]:>10.2f}")


main()
