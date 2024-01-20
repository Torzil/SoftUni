number = float(input())
number_is_negative = False

while True:
    if number < 0:
        number_is_negative = True
        break
    result = number * 2
    print(f"Result: {result:.2f}")

    number = float(input())

if number_is_negative:
    print("Negative number!")
