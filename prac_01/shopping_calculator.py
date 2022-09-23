total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items <= 0:
    print("Invalid number!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price = int(input("Price of item: "))
    total_price = total_price + price
print(f"The total price for the {number_of_items} items is ${total_price}")