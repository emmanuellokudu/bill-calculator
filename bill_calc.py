price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))

total_cost = price * quantity

print(f"{quantity} items at KES {price:.2f} each = KES {total_cost:.2f}")