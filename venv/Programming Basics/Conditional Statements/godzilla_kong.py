movie_budget = float(input())
number_of_extras = int(input())
costume_price = float(input())
decor_price = movie_budget * 0.1

if number_of_extras > 150:
    costume_price -= costume_price * 0.1

total_price = number_of_extras * costume_price + decor_price

difference = abs(total_price - movie_budget)

if movie_budget >= total_price:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
