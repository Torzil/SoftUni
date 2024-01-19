from math import pi, pow

r = float(input())

circle_area = pi * pow(r, 2)
circle_perimeter = 2 * pi * r

print(format(circle_area, '.2f'))
print(format(circle_perimeter, '.2f'))