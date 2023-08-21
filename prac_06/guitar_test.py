"""CP1404/CP5632 Practical - Client code to test the Guitar class.
Estimate: 15 minutes
Time started: 11:41
Time finished:
"""

from cp1404practicals.prac_06.guitar import Guitar


def main():
    """Test Guitar class."""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013)
    print(f"{gibson.name} get_age() - Expected 101. Got {gibson.get_age()}\n{another_guitar.name} get_age() - Expected"
          f" 10. Got {another_guitar.get_age()}")
    print(
        f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}\n{another_guitar.name} is_vintage() - "
        f"Expected False. Got {another_guitar.is_vintage()}")


if __name__ == '__main__':
    main()
