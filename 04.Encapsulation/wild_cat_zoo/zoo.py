class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.animals = []
        self.workers = []
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

    def add_animal(self, animal, price):
        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif len(self.animals) < self.__animal_capacity and self.__budget < price:
            return f"Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        worker = [w for w in self.workers if w.name == worker_name]
        if worker:
            self.workers.remove(worker[0])
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        all_saraies_to_pay = sum([w.salary for w in self.workers])
        if self.__budget >= all_saraies_to_pay:
            self.__budget -= all_saraies_to_pay
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        all_cost_for_tending_animals = sum([a.get_needs() for a in self.animals])
        if self.__budget >= all_cost_for_tending_animals:
            self.__budget -= all_cost_for_tending_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]

        result = f"You have {len(self.animals)} animals" + "\n"
        result += f"----- {len(lions)} Lions:" + "\n"
        result += "{}".format('\n'.join([repr(l) for l in lions])) + "\n"
        result += f"----- {len(tigers)} Tigers:" + "\n"
        result += "{}".format('\n'.join([repr(t) for t in tigers])) + "\n"
        result += f"----- {len(cheetahs)} Cheetahs:" + "\n"
        result += "{}".format('\n'.join([repr(c) for c in cheetahs]))
        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers" + "\n"

        keepers = [w for w in self.workers if w.__class__.__name__ == "Keeper"]
        caretakers = [w for w in self.workers if w.__class__.__name__ == "Caretaker"]
        vets = [w for w in self.workers if w.__class__.__name__ == "Vet"]

        result += f"----- {len(keepers)} Keepers:\n"
        result += "{}".format('\n'.join([repr(w) for w in keepers])) + "\n"
        result += f"----- {len(caretakers)} Caretakers:\n"
        result += "{}".format('\n'.join([repr(w) for w in caretakers])) + "\n"
        result += f"----- {len(vets)} Vets:\n"
        result += "{}".format('\n'.join([repr(w) for w in vets]))
        return result
