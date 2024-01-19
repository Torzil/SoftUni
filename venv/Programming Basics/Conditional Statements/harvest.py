from math import floor, ceil

vineyard_size = int(input())
grapes_per_sq_meter = float(input())
needed_liters_wine = int(input())
workers_number = int(input())

grapes_for_wine = (vineyard_size * grapes_per_sq_meter) * 0.4
produced_wine = grapes_for_wine / 2.5
difference = abs(needed_liters_wine - produced_wine)

if produced_wine < needed_liters_wine:
    print(f"It will be a tough winter! More {floor(difference)} liters wine needed.")
elif produced_wine >= needed_liters_wine:
    extra_wine = difference / workers_number
    print(f"Good harvest this year! Total wine: {floor(produced_wine)} liters.")
    print(f"{ceil(difference)} liters left -> {ceil(extra_wine)} liters per person.")
