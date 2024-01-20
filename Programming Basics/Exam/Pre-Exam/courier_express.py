package_weight = float(input())
delivery_type = input()
travel_distance = int(input())
price_per_kilometer = 0
overcharge_per_kilogram = 0
overcharge_per_kilometer = 0
total_overcharge = 0

if package_weight < 1:
    price_per_kilometer = 0.03
elif package_weight < 10:
    price_per_kilometer = 0.05
elif package_weight < 40:
    price_per_kilometer = 0.10
elif package_weight < 90:
    price_per_kilometer = 0.15
elif package_weight < 150:
    price_per_kilometer = 0.20

if delivery_type == "express":
    if package_weight < 1:
        overcharge_per_kilogram = price_per_kilometer * 0.8
        overcharge_per_kilometer = overcharge_per_kilogram * package_weight
        total_overcharge = travel_distance * overcharge_per_kilometer
    elif package_weight < 10:
        overcharge_per_kilogram = price_per_kilometer * 0.4
        overcharge_per_kilometer = overcharge_per_kilogram * package_weight
        total_overcharge = travel_distance * overcharge_per_kilometer
    elif package_weight < 40:
        overcharge_per_kilogram = price_per_kilometer * 0.05
        overcharge_per_kilometer = overcharge_per_kilogram * package_weight
        total_overcharge = travel_distance * overcharge_per_kilometer
    elif package_weight < 90:
        overcharge_per_kilogram = price_per_kilometer * 0.02
        overcharge_per_kilometer = overcharge_per_kilogram * package_weight
        total_overcharge = travel_distance * overcharge_per_kilometer
    elif package_weight < 150:
        overcharge_per_kilogram = price_per_kilometer * 0.01
        overcharge_per_kilometer = overcharge_per_kilogram * package_weight
        total_overcharge = travel_distance * overcharge_per_kilometer

total_price = price_per_kilometer * travel_distance + total_overcharge

print(f"The delivery of your shipment with weight of {package_weight:.3f} kg. would cost {total_price:.2f} lv.")
