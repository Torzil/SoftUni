number_of_computers = int(input())
rating_sum = 0
total_sales = 0

for computer in range(number_of_computers):
    special_number = input()
    rating = int(special_number[2])
    sales = int(special_number[0] + special_number[1])
    if rating == 2:
        sales *= 0
    elif rating == 3:
        sales *= 0.5
    elif rating == 4:
        sales *= 0.7
    elif rating == 5:
        sales *= 0.85
    elif rating == 6:
        sales *= 1
    rating_sum += rating
    total_sales += sales

average_rating = rating_sum / number_of_computers

print(f"{total_sales:.2f}")
print(f"{average_rating:.2f}")
