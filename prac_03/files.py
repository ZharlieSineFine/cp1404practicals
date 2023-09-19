"""Prac_03 files.py"""
# Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
user_name = input("Name: ")
out_file = open('name.txt', 'w')
print(user_name, file=out_file)
out_file.close()

# Write code that opens "name.txt" and reads the name (as above) then prints,"Your name is Bob"
# (or whatever the name is in the file).
in_file = open('name.txt')
user_name = in_file.read()
print(f"Your name is {user_name}")
in_file.close()

# Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result,
# which should be... 59.
in_file = open('numbers.txt')
x = int(in_file.readline())
y = int(in_file.readline())
in_file.close()
print(f"The result is {x + y}")

# Now write a fourth block of code that prints the total for all lines in numbers.txt or a file
# with any number of numbers.
INPUT_FILE = 'numbers.txt'
in_file = open(INPUT_FILE)

total = 0
for line in in_file:
    number = int(line)
    total += number
print(f"The total of {INPUT_FILE} is {total}.")
in_file.close()
