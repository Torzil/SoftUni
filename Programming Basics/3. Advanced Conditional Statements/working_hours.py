time = int(input())
day = input()

if 10 <= time <= 18:
    if day.lower() == "sunday":
        print("closed")
    else:
        print("open")
else:
    print("closed")
