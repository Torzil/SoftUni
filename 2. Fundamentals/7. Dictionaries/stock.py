ingredients_and_quantities = input().split()
searched_items = input().split()
stock = {}

for i in range(0, len(ingredients_and_quantities), 2):
    ingredient = ingredients_and_quantities[i]
    quantity = ingredients_and_quantities[i + 1]
    stock[ingredient] = int(quantity)

for item in searched_items:
    if item in stock.keys():
        print(f"We have {stock[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
