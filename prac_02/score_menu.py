"""CP1404 practical 2 - score menu"""

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100


def main():
    """Get option and execute."""
    score = -1
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(result)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def get_valid_score():
    """Get a valid score."""
    score = int(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


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


def show_stars(score):
    """Show stars of the same length as the score."""
    print("*" * score)


main()
