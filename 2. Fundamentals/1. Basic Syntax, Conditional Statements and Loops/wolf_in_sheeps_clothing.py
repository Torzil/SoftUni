animals = input()
flock = animals.split()
flock.reverse()
wolf_position = 0

if "wolf" in flock:
    wolf_position = flock.index("wolf")
elif "wolf," in flock:
    wolf_position = flock.index("wolf,")
if wolf_position == 0:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {wolf_position}! You are about to be eaten by a wolf!")
