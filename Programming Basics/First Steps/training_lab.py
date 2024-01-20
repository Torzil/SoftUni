from math import floor

h = float(input())
w = float(input())

h1 = (h * 100) // 120
w1 = (w * 100 - 100) // 70

total_seats = h1 * w1 - 3

print (floor(total_seats))
