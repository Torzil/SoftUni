sea_excursions_number = int(input())
mountain_excursions_number = int(input())
total_profits = 0
everything_is_sold = False

current_excursion = input()
while current_excursion != "Stop":
    if current_excursion == "sea":
        sea_excursions_number -= 1
        if sea_excursions_number < 0:
            total_profits += 0
        else:
            total_profits += 680
    elif current_excursion == "mountain":
        mountain_excursions_number -= 1
        if mountain_excursions_number < 0:
            total_profits += 0
        else:
            total_profits += 499
    if sea_excursions_number <= 0 and mountain_excursions_number <= 0:
        everything_is_sold = True
        break
    current_excursion = input()

if everything_is_sold:
    print("Good job! Everything is sold.")

print(f"Profit: {total_profits} leva.")
