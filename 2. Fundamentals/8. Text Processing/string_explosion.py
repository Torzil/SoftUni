initial_string = input()
exploded_string = ""
explosion_strength = 0

for index in range(len(initial_string)):
    # Explosion
    if initial_string[index] != ">" and explosion_strength > 0:
        explosion_strength -= 1
    # > mark
    elif initial_string[index] == ">":
        exploded_string += ">"
        explosion_strength += int(initial_string[index + 1])
    # No explosion, no > mark
    else:
        exploded_string += initial_string[index]

print(exploded_string)
