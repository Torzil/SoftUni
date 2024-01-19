speed = float(input())

if speed > 1000:
    print("extremely fast")
elif 150 < speed <= 1000:
    print("ultra fast" )
elif 50 < speed <= 150:
    print("fast")
elif 10 < speed <= 50:
    print("average")
else:
    print("slow")
