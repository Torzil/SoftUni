required_profits = float(input())
current_profits = 0
target_reached = False

cocktail_name = input()
while cocktail_name != "Party!":
    number_of_cocktails = int(input())
    order_price = len(cocktail_name) * number_of_cocktails
    if order_price % 2 != 0:
        order_price *= 0.75
    current_profits += order_price
    if current_profits >= required_profits:
        target_reached = True
        break
    cocktail_name = input()

if target_reached:
    print("Target acquired.")
    print(f"Club income - {current_profits:.2f} leva.")
else:
    difference = required_profits - current_profits
    print(f"We need {difference:.2f} leva more.")
    print(f"Club income - {current_profits:.2f} leva.")
