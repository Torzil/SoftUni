number_of_loads_to_be_transported = int(input())
total_transport_price = 0
total_tons_transported = 0
price_per_ton = 0
van_tons_transported = 0
truck_tons_transported = 0
train_tons_transported = 0

for load in range(number_of_loads_to_be_transported):
    current_load_weight = int(input())
    if current_load_weight <= 3:
        price_per_ton = 200
        van_tons_transported += current_load_weight
    elif current_load_weight <= 11:
        price_per_ton = 175
        truck_tons_transported += current_load_weight
    elif current_load_weight >= 12:
        price_per_ton = 120
        train_tons_transported += current_load_weight
    total_tons_transported += current_load_weight
    total_transport_price += current_load_weight * price_per_ton

average_price_per_ton_transported = total_transport_price / total_tons_transported
percentage_van_tons_transported = van_tons_transported / total_tons_transported * 100
percentage_truck_tons_transported = truck_tons_transported / total_tons_transported * 100
percentage_train_tons_transported = train_tons_transported / total_tons_transported * 100

print(f"{average_price_per_ton_transported:.2f}")
print(f"{percentage_van_tons_transported:.2f}%")
print(f"{percentage_truck_tons_transported:.2f}%")
print(f"{percentage_train_tons_transported:.2f}%")
