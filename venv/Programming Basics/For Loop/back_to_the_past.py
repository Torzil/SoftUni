inherited_money = float(input())
year_to_live_to = int(input())
current_age = 18

for year in range(1800, year_to_live_to + 1):
    if year % 2 == 0:
        inherited_money -= 12000
    else:
        inherited_money -= 12000 + 50 * current_age
    current_age += 1

difference = abs(inherited_money)

if inherited_money >= 0:
    print(f"Yes! He will live a carefree life and will have {difference:.2f} dollars left.")
else:
    print(f"He will need {difference:.2f} dollars to survive.")
