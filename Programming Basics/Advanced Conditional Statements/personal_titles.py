age = float(input())
sex = input()

if sex.lower() == "m":
    if age >= 16:
        print("Mr.")
    else:
        print("Master")
elif sex.lower() == "f":
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")
