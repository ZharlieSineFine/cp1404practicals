"""

total_price = 0
get number_of_items
while number_of_items < 0
    print error
    get number_of_items
for i in range(number_of_items)
    get price_of_item
    total_price = total_price + price_of_item
if total_price > 100
    total_price = total_price * (1 - 0.1)
print total_price

"""
DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.1

total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price += price_of_item
if total_price > DISCOUNT_THRESHOLD:
    total_price *= (1 - DISCOUNT_RATE)
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
