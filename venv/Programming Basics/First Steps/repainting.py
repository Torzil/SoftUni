needed_nylon = int(input())
needed_paint = int(input())
needed_thinner = int(input())
worker_hours = int(input())

nylon_price = 1.50
paint_price = 14.50
thinner_price = 5.00

materials_sum = (needed_nylon + 2) * nylon_price \
    + (needed_paint * paint_price) * 1.1 \
    + (needed_thinner * thinner_price) + 0.40
total_sum = (materials_sum * 0.3) * worker_hours + materials_sum

print(total_sum)