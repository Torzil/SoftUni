coffees_needed = 0

event = input()
while event != "END":
    if event.lower() in "coding, dog, cat, movie":
        if event.isupper():
            coffees_needed += 2
        elif event.islower():
            coffees_needed += 1
    event = input()

if coffees_needed > 5:
    print("You need extra sleep")
else:
    print(coffees_needed)
