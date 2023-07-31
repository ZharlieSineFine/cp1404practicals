"""Write a program that prompts the user for 5 numbers and then stores each of these in a list called numbers."""

NUMBER_OF_PROMPTS = 5


def main():
    """Get numbers and display info."""
    numbers = []
    total = 0
    for i in range(NUMBER_OF_PROMPTS):
        number = int(input("Number: "))
        numbers.append(number)
        total += number

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {total / NUMBER_OF_PROMPTS:.1f}")


main()
