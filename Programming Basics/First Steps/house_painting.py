x = float(input())
y = float(input())
h = float(input())

front_back_walls_area = (x * x) * 2 - (1.2 * 2)
side_walls_area = (x * y) * 2 - (1.5 * 1.5) * 2
total_walls_area = front_back_walls_area + side_walls_area

roof_sides_area = (x * y) * 2
roof_front_back_area = ((x * h) / 2) * 2
total_roof_area = roof_sides_area + roof_front_back_area

green_paint_needed = total_walls_area / 3.4
red_paint_needed = total_roof_area / 4.3

print(format(green_paint_needed, '.2f'))
print(format(red_paint_needed, '.2f'))