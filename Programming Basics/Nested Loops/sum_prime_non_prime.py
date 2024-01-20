prime_numbers_sum = 0
non_prime_numbers_sum = 0

current_number = input()
while current_number != "stop":
    current_number = int(current_number)
    if current_number < 0:
        print("Number is negative.")
    else:
        number_is_prime = True
        for number in range(2, current_number):
            if current_number % number == 0:
                number_is_prime = False
                break
        if number_is_prime:
            prime_numbers_sum += current_number
        else:
            non_prime_numbers_sum += current_number

    current_number = input()

print(f"Sum of all prime numbers is: {prime_numbers_sum}")
print(f"Sum of all non prime numbers is: {non_prime_numbers_sum}")
