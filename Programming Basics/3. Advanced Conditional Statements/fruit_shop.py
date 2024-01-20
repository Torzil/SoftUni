fruit = input()
day = input()
amount = float(input())

valid_input = True
total_price = 0
banana_price = 0
apple_price = 0
orange_price = 0
grapefruit_price = 0
kiwi_price = 0
pineapple_price = 0
grapes_price = 0

if day.lower() == "monday" or day.lower() == "tuesday" or day.lower() == "wednesday" \
        or day.lower() == "thursday" or day.lower() == "friday":
    banana_price = 2.50
    apple_price = 1.20
    orange_price = 0.85
    grapefruit_price = 1.45
    kiwi_price = 2.70
    pineapple_price = 5.50
    grapes_price = 3.85
elif day.lower() == "saturday" or day.lower() == "sunday":
    banana_price = 2.70
    apple_price = 1.25
    orange_price = 0.90
    grapefruit_price = 1.60
    kiwi_price = 3.00
    pineapple_price = 5.60
    grapes_price = 4.20
else:
    print("error")
    exit()

if fruit.lower() == "banana":
    total_price = amount * banana_price
    print(f"{total_price:.2f}")
elif fruit.lower() == "apple":
    total_price = amount * apple_price
    print(f"{total_price:.2f}")
elif fruit.lower() == "orange":
    total_price = amount * orange_price
    print(f"{total_price:.2f}")
elif fruit.lower() == "grapefruit":
    total_price = amount * grapefruit_price
    print(f"{total_price:.2f}")
elif fruit.lower() == "kiwi":
    total_price = amount * kiwi_price
    print(f"{total_price:.2f}")
elif fruit.lower() == "pineapple":
    total_price = amount * pineapple_price
    print(f"{total_price:.2f}")
elif fruit.lower() == "grapes":
    total_price = amount * grapes_price
    print(f"{total_price:.2f}")
else:
    print("error")
