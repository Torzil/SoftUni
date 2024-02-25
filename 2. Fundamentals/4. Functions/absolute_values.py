values_as_string = input().split()
values_as_int = [float(value) for value in values_as_string]
absolute_values = list(map(abs, values_as_int))

print(absolute_values)
