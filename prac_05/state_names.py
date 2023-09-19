"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()  # Change the input to uppercase
while state_code != "":
    # if state_code in CODE_TO_NAME:
    #     print(state_code, "is", CODE_TO_NAME[state_code])
    # else:
    #     print("Invalid short state")
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

# Write a loop that prints all the states and names neatly lined up with string formatting
# Add maximum length for state code
code_maximum_length = max(len(code) for code in list(CODE_TO_NAME.keys()))
name_maximum_length = max(len(name) for name in list(CODE_TO_NAME.values()))
for code, name in CODE_TO_NAME.items():
    print(f"{code:<{code_maximum_length}} is {name:<{name_maximum_length}}")
