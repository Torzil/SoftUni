budget = int(input())
season = input()
fishermen_number = int(input())

boat_rent = 0

if season == "Spring":
    boat_rent = 3000
elif season == "Summer" or season == "Autumn":
    boat_rent = 4200
elif season == "Winter":
    boat_rent = 2600

if fishermen_number <= 6:
    boat_rent *= 0.9
elif fishermen_number <= 11:
    boat_rent *= 0.85
elif fishermen_number >= 12:
    boat_rent *= 0.75

if fishermen_number % 2 == 0 and season != "Autumn":
    boat_rent *= 0.95

difference = abs(budget - boat_rent)

if budget >= boat_rent:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
