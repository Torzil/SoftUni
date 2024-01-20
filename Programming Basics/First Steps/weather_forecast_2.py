temperature = float(input())
if temperature > 35.00:
    weather = ("unknown")
    print(weather)
elif temperature == 35.00:
    weather = ("Hot")
    print(weather)
elif temperature >= 26.00:
    weather = ("Hot")
    print (weather)
elif temperature >= 20.1:
    weather = ("Warm")
    print(weather)
elif temperature >= 15.00:
    weather = ("Mild")
    print(weather)
elif temperature >= 12.00:
    weather = ("Cool")
    print(weather)
elif temperature >= 5.00:
    weather = ("Cold")
    print(weather)
else:
    print("unknown")