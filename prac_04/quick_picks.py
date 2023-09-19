"""Write a program that asks the user how many "quick picks" they wish to generate.
The program then generates that many lines of output. Each line consists of 6 random numbers between 1 and 45.
Each line (quick pick) should not contain any repeated number.
Each line of numbers should be displayed in sorted (ascending) order.
Note the formatting below so that numbers align neatly."""

import random

NUMBER_OF_RANDOM_NUMBERS = 6
RANDOM_MINIMUM = 1
RANDOM_MAXIMUM = 45

number_of_lines = int(input("How many quick picks? "))

for i in range(number_of_lines):
    numbers = []
    for j in range(NUMBER_OF_RANDOM_NUMBERS):
        new_number = random.randint(RANDOM_MINIMUM, RANDOM_MAXIMUM)
        while new_number in numbers:
            new_number = random.randint(RANDOM_MINIMUM, RANDOM_MAXIMUM)
        numbers.append(new_number)
    numbers.sort()
    print(" ".join(f"{number:2}" for number in numbers))
