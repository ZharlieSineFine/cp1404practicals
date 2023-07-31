"""Write a program that prompts the user for 5 numbers and then stores each of these in a list called numbers."""

NUMBER_OF_PROMPTS = 5


def main():
    """Get numbers and display info."""
    numbers = []
    for i in range(NUMBER_OF_PROMPTS):
        number = int(input("Number: "))
        numbers.append(number)

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / NUMBER_OF_PROMPTS:.1f}")

    # Woefully inadequate security checker
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    user_name = input("Username: ")
    if user_name in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()
