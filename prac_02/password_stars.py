"""This program checks password and return asteriks of the same length as the password."""
MINIMUM_LENGTH = 8


def main():
    """Get password and print asterisks."""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    """Get password and check if it is long enough."""
    password = input("Enter password: ")
    while len(password) < minimum_length:
        print("Password is too short")
        password = input("Enter password: ")
    return password


def print_asterisks(password):
    """Print asterisks of the same length as the password."""
    print("*" * len(password))


main()
