product = input()
city = input()
amount = float(input())

price = 0

if city.lower() == "sofia":
    if product.lower() == "coffee":
        price = 0.50
    elif product.lower() == "water":
        price = 0.80
    elif product.lower() == "beer":
        price = 1.20
    elif product.lower() == "sweets":
        price = 1.45
    elif product.lower() == "peanuts":
        price = 1.60
elif city.lower() == "plovdiv":
    if product.lower() == "coffee":
        price = 0.40
    elif product.lower() == "water":
        price = 0.70
    elif product.lower() == "beer":
        price = 1.15
    elif product.lower() == "sweets":
        price = 1.30
    elif product.lower() == "peanuts":
        price = 1.50
elif city.lower() == "varna":
    if product.lower() == "coffee":
        price = 0.45
    elif product.lower() == "water":
        price = 0.70
    elif product.lower() == "beer":
        price = 1.10
    elif product.lower() == "sweets":
        price = 1.35
    elif product.lower() == "peanuts":
        price = 1.55

total_price = price * amount
print(total_price)
