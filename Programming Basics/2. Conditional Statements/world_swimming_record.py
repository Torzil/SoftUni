record_time = float(input())
distance = float(input())
one_meter_time = float(input())

water_resistance_delay = (distance // 15) * 12.5

swimming_time = distance * one_meter_time + water_resistance_delay

difference = abs(record_time - swimming_time)

if swimming_time < record_time:
    print(f"Yes, he succeeded! The new world record is {swimming_time:.2f} seconds.")
elif swimming_time >= record_time:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")
