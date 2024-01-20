from math import pi

shape_type = input()
area = 0

if shape_type == "square":
    a = float(input())
    area = a * a
elif shape_type == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
elif shape_type == "circle":
    r = float(input())
    area = pi * r ** 2
elif shape_type == "triangle":
    a = float(input())
    h = float(input())
    area = a * h / 2

print(f"{area:.3f}")
