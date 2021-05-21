class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, specie, name):
        if specie == "mammal":
            self.mammals.append(name)
        elif specie == "fish":
            self.fishes.append(name)
        elif specie == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, specie):
        if specie == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {self.__animals}"
        elif specie == "fish":
            return f"Fishes in {self.name}: {', '.join(self.fishes)}\nTotal animals: {self.__animals}"
        elif specie == "bird":
            return f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {self.__animals}"


zoo_name = input()
current_zoo = Zoo(zoo_name)
n = int(input())

for _ in range(n):
    specie, animal = input().split()
    current_zoo.add_animal(specie, animal)

species = input()
print(current_zoo.get_info(species))
