"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
from random import *


def main():
    """Get score and print status."""
    score = float(input("Enter score: "))
    result = determine_result(score)

    print(result)

    random_score = randint(0, 100)
    random_result = determine_result(random_score)
    print(f"A random score of {random_score} is {random_result}")


def determine_result(score):
    """Determine result based on score."""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
