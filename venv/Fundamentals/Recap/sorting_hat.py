name = input()
house = ""
he_has_been_mentioned = False
while name != "Welcome!":
    if name == "Voldemort":
        he_has_been_mentioned = True
        print("You must not speak of that name!")
        break
    if len(name) < 5:
        house = "Gryffindor"
    elif len(name) == 5:
        house = "Slytherin"
    elif len(name) == 6:
        house = "Ravenclaw"
    elif len(name) > 6:
        house = "Hufflepuff"
    print(f"{name} goes to {house}.")
    name = input()

if not he_has_been_mentioned:
    print("Welcome to Hogwarts.")
