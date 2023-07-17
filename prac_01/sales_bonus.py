"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
BONUS_THRESHOLD = 1000
BELOW_BONUS = 0.1
OVER_BONUS = 0.15

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < BONUS_THRESHOLD:
        bonus = sales * BELOW_BONUS
    else:
        bonus = sales * OVER_BONUS
    print(f"The bonus is ${bonus}")
    sales = float(input("Enter sales: $"))
print("Bye!")
