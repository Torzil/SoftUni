countries = input().split(", ")
cities = input().split(", ")

capitals = dict(zip(countries, cities))

for country, capital in capitals.items():
    print(f"{country} -> {capital}")
