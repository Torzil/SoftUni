deposit = float(input())
deposit_duration = int(input())
annualised_interest_rate = float(input())

monthly_interest_rate = deposit * (annualised_interest_rate / 100) / 12
total_interest_paid = deposit + monthly_interest_rate * deposit_duration

print(total_interest_paid)
