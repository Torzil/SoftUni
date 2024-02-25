def order_calculator(product, amount):
    if product == "coffee":
        price = 1.50
    elif product == "water":
        price = 1.00
    elif product == "coke":
        price = 1.40
    elif product == "snacks":
        price = 2.00
    return price * amount


item = input()
amount_of_item = int(input())

print(f"{order_calculator(item, amount_of_item):.2f}")
