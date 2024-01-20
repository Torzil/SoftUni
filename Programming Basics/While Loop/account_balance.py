total_account_balance = 0

while True:
    current_payment = input()

    if current_payment == "NoMoreMoney":
        break

    current_payment = float(current_payment)

    if current_payment <= 0:
        print("Invalid operation!")
        break
    else:
        total_account_balance += current_payment
        print(f"Increase: {current_payment:.2f}")

print(f"Total: {total_account_balance:.2f}")
