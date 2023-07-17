minimum_length = 8

password = input("Enter password: ")
while len(password) < minimum_length:
    print("Password is too short")
    password = input("Enter password: ")
print("*" * len(password))
