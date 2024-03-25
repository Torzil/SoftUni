class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, animal_name):
        if species == "mammal":
            self.mammals.append(animal_name)
        elif species == "fish":
            self.fishes.append(animal_name)
        elif species == "bird":
            self.birds.append(animal_name)

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}"
        elif species == "fish":
            return f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}"
        elif species == "bird":
            return f"Birds in {self.zoo_name}: {', '.join(self.birds)}"


name_of_zoo = input()
number_of_animals = int(input())

zoo = Zoo(name_of_zoo)

for animal in range(number_of_animals):
    current_animal = input().split()
    zoo.add_animal(current_animal[0], current_animal[1])

species_to_check = input()

print(zoo.get_info(species_to_check))
print(f"Total animals: {number_of_animals}")
