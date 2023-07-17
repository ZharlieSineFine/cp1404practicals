MENU = '(E)ven numbers\n(O)dd numbers\n(S)quares\n(Q)uit'

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
while y <= x:
    print("y has to be greater than x")
print(MENU)
user_option = input(">>> ").upper()

while user_option != 'Q':
    if user_option == 'E':
        for i in range(x, y + 1):
            if i % 2 == 0:
                print(i, end=' ')
        print()
    elif user_option == 'O':
        for i in range(x, y + 1):
            if i % 2 == 1:
                print(i, end=' ')
        print()
    elif user_option == 'S':
        for i in range(x, y + 1):
            print(i ** 2, end=' ')
        print()
    else:
        print("Invalid option.")
    print(MENU)
    user_option = input(">>> ").upper()
