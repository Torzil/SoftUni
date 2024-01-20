baggage_price_over_20kg = float(input())
baggage_kilograms = float(input())
days_to_departure = int(input())
number_of_bags = int(input())
baggage_fee = 0

if baggage_kilograms < 10:
    baggage_fee = baggage_price_over_20kg * 0.2
elif baggage_kilograms in range(10, 21):
    baggage_fee = baggage_price_over_20kg * 0.5
elif baggage_kilograms > 20:
    baggage_fee = baggage_price_over_20kg

if days_to_departure > 30:
    baggage_fee = baggage_fee * 1.1
elif days_to_departure in range(7, 31):
    baggage_fee = baggage_fee * 1.15
elif days_to_departure < 7:
    baggage_fee = baggage_fee * 1.4

total_price = number_of_bags * baggage_fee
total_price = format(total_price, '.2f')

print(f"The total price of bags is: {total_price} lv.")
