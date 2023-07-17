"""
CP1404/CP5632 - Practical
Use score to determine result
"""
from random import *
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50


def main():
    """Get score and print result."""
    score = float(input("Enter score: "))
    result = determine_result(score)

    print(result)

    random_score = randint(MINIMUM_SCORE, MAXIMUM_SCORE)
    random_result = determine_result(random_score)
    print(f"A random score of {random_score} is {random_result}")


def determine_result(score):
    """Determine result based on score."""
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        result = "Invalid score"
    elif score >= EXCELLENT_THRESHOLD:
        result = "Excellent"
    elif score >= PASSABLE_THRESHOLD:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
