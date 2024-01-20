from math import ceil

number_of_people = int(input())
entry_fee = float(input())
sunbed_fee = float(input())
umbrella_fee = float(input())

number_of_umbrellas = ceil(number_of_people / 2)
number_of_sunbeds = ceil(number_of_people * 0.75)

total_price = number_of_people * entry_fee\
    + number_of_umbrellas * umbrella_fee \
    + number_of_sunbeds * sunbed_fee

print(f"{total_price:.2f} lv.")
