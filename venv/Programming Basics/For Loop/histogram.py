numbers_amount = int(input())
p1_sum = 0
p2_sum = 0
p3_sum = 0
p4_sum = 0
p5_sum = 0

for number in range(numbers_amount):
    current_number = int(input())
    if current_number < 200:
        p1_sum += 1
    elif current_number < 400:
        p2_sum += 1
    elif current_number < 600:
        p3_sum += 1
    elif current_number < 800:
        p4_sum += 1
    elif current_number >= 800:
        p5_sum += 1

p1_percentage = p1_sum / numbers_amount * 100
p2_percentage = p2_sum / numbers_amount * 100
p3_percentage = p3_sum / numbers_amount * 100
p4_percentage = p4_sum / numbers_amount * 100
p5_percentage = p5_sum / numbers_amount * 100

print(f"{p1_percentage:.2f}%")
print(f"{p2_percentage:.2f}%")
print(f"{p3_percentage:.2f}%")
print(f"{p4_percentage:.2f}%")
print(f"{p5_percentage:.2f}%")
