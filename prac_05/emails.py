"""
Emails
Estimate: 15 minutes
Actual:   25 minutes
"""


def main():
    user_email = input("Email: ")
    email_to_name = {}
    while user_email != "":
        user_name = extract_name_by_email(user_email)
        name_answer = input(f"Is your name {user_name.title()}? (Y/n) ").upper()
        if name_answer != "" and name_answer != "Y":
            user_name = input("Name: ")

        email_to_name[user_email] = user_name

        user_email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_by_email(email):
    name_components = email.split("@")[0].split(".")
    user_name = " ".join(name_components).title()
    return user_name


main()
