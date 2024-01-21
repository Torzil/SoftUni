first_number = int(input())
second_number = int(input())

old_first_number = first_number
old_second_number = second_number

first_number = old_second_number
second_number = old_first_number

print("Before:")
print(f"a = {old_first_number}")
print(f"b = {old_second_number}")
print("After:")
print(f"a = {first_number}")
print(f"b = {second_number}")
