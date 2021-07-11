class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity:
            if self.__budget >= price:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_needed = sum([worker.salary for worker in self.workers])
        if sum_needed <= self.__budget:
            self.__budget -= sum_needed
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        sum_needed = sum([animal.money_for_care for animal in self.animals])
        if sum_needed <= self.__budget:
            self.__budget -= sum_needed
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = []
        tigers = []
        cheetahs = []

        for animal in self.animals:
            if animal.__class__.__name__ == 'Lion':
                lions.append(animal)
            elif animal.__class__.__name__ == 'Tiger':
                tigers.append(animal)
            elif animal.__class__.__name__ == 'Cheetah':
                cheetahs.append(animal)

        result = f"You have {len(self.animals)} animals\n"
        result += f"----- {len(lions)} Lions:\n"
        result += "\n".join([lion.__repr__() for lion in lions])
        result += f"\n----- {len(tigers)} Tigers:\n"
        result += "\n".join([tiger.__repr__() for tiger in tigers])
        result += f"\n----- {len(cheetahs)} Cheetahs:\n"
        result += "\n".join([cheetah.__repr__() for cheetah in cheetahs])

        return result

    def workers_status(self):
        caretakers = []
        keepers = []
        vets = []

        for worker in self.workers:
            if worker.__class__.__name__ == 'Caretaker':
                caretakers.append(worker)
            elif worker.__class__.__name__ == 'Keeper':
                keepers.append(worker)
            elif worker.__class__.__name__ == 'Vet':
                vets.append(worker)

        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {len(keepers)} Keepers:\n"
        result += "\n".join([keeper.__repr__() for keeper in keepers])
        result += f"\n----- {len(caretakers)} Caretakers:\n"
        result += "\n".join([caretaker.__repr__() for caretaker in caretakers])
        result += f"\n----- {len(vets)} Vets:\n"
        result += "\n".join([vet.__repr__() for vet in vets])

        return result
