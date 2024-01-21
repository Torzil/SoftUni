total_lines = int(input())
total_sum = 0

for line in range(total_lines):
    current_line = input()
    total_sum += ord(current_line)

print(f"The sum equals: {total_sum}")
