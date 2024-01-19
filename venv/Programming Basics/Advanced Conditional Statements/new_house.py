flower_type = input()
number_of_flowers = int(input())
budget = int(input())

rose_price = 5
dahlia_price = 3.80
tulip_price = 2.80
narcissus_price = 3
gladiolus_price = 2.50
total_price = 0

if flower_type == "Roses":
    total_price = number_of_flowers * rose_price
    if number_of_flowers > 80:
        total_price *= 0.9
elif flower_type == "Dahlias":
    total_price = number_of_flowers * dahlia_price
    if number_of_flowers > 90:
        total_price *= 0.85
elif flower_type == "Tulips":
    total_price = number_of_flowers * tulip_price
    if number_of_flowers > 80:
        total_price *= 0.85
elif flower_type == "Narcissus":
    total_price = number_of_flowers * narcissus_price
    if number_of_flowers < 120:
        total_price *= 1.15
elif flower_type == "Gladiolus":
    total_price = number_of_flowers * gladiolus_price
    if number_of_flowers < 80:
        total_price *= 1.20

difference = abs(budget - total_price)
if budget >= total_price:
    print(f"Hey, you have a great garden with {number_of_flowers} {flower_type} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
