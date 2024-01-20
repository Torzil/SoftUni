total_months = int(input())
total_electricity_bill = 0
total_water_bill = 0
total_internet_bill = 0
total_others_bills = 0
total_bills = 0

for month in range(total_months):
    total_bills_this_month = 0
    current_electricity_bill = float(input())
    total_electricity_bill += current_electricity_bill
    total_bills_this_month += current_electricity_bill
    total_water_bill += 20
    total_bills_this_month += 20
    total_internet_bill += 15
    total_bills_this_month += 15
    current_others_bills = total_bills_this_month * 1.2
    total_others_bills += current_others_bills
    total_bills += total_bills_this_month + current_others_bills

average_bills_per_month = total_bills / total_months

print(f"Electricity: {total_electricity_bill:.2f} lv")
print(f"Water: {total_water_bill:.2f} lv")
print(f"Internet: {total_internet_bill:.2f} lv")
print(f"Other: {total_others_bills:.2f} lv")
print(f"Average: {average_bills_per_month:.2f} lv")
