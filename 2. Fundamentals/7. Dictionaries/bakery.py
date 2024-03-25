ingredients_and_quantities = input().split()
stock = {}

for i in range(0, len(ingredients_and_quantities), 2):
    ingredient = ingredients_and_quantities[i]
    quantity = ingredients_and_quantities[i + 1]
    stock[ingredient] = int(quantity)

print(stock)
