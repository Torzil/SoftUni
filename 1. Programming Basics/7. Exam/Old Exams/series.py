budget = float(input())
number_of_series = int(input())
total_price = 0

for series in range(number_of_series):
    series_name = input()
    series_price = float(input())
    if series_name == "Thrones":
        series_price *= 0.5
    elif series_name == "Lucifer":
        series_price *= 0.6
    elif series_name == "Protector":
        series_price *= 0.7
    elif series_name == "TotalDrama":
        series_price *= 0.8
    elif series_name == "Area":
        series_price *= 0.9
    total_price += series_price

difference = f"{abs(budget - total_price):.2f}"

if total_price <= budget:
    print(f"You bought all the series and left with {difference} lv.")
else:
    print(f"You need {difference} lv. more to buy the series!")
