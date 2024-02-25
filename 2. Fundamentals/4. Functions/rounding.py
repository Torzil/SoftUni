values = input().split()

float_values = list(map(float, values))
rounded_values = list(map(round, float_values))

print(rounded_values)
