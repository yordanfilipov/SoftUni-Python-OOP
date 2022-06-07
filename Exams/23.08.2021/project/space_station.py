from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.unsuccessful_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        valid_types = ["Biologist", "Geodesist", "Meteorologist"]
        astronaut = [a for a in self.astronaut_repository.astronauts if a.name == name]
        if astronaut:
            return f"{name} is already added."
        if astronaut_type not in valid_types:
            raise Exception('Astronaut type is not valid!')
        if astronaut_type == "Biologist":
            astronaut = Biologist(name)
        elif astronaut_type == "Geodesist":
            astronaut = Geodesist(name)
        else:
            astronaut = Meteorologist(name)
        self.astronaut_repository.astronauts.append(astronaut)
        return f'Successfully added {astronaut_type}: {name}.'

    def add_planet(self, name: str, items: str):
        planet = [p for p in self.planet_repository.planets if p.name == name]
        if planet:
            return f"{name} is already added."
        planet = Planet(name)
        list_items = items.split(", ")
        for i in list_items:
            planet.items.append(i)
        self.planet_repository.planets.append(planet)
        return f'Successfully added Planet: {name}.'

    def retire_astronaut(self, name: str):
        astronaut = [a for a in self.astronaut_repository.astronauts if a.name == name]
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")
        astronaut = astronaut[0]
        self.astronaut_repository.astronauts.remove(astronaut)
        return f'Astronaut {name} was retired!'

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name: str):
        astronauts_in_open_space = 0
        planet = [p for p in self.planet_repository.planets if p.name == planet_name]
        if not planet:
            raise Exception("Invalid planet name!")
        planet = planet[0]
        available_astronauts = []
        for a in self.astronaut_repository.astronauts:
            if a.oxygen > 30:
                available_astronauts.append(a)
        available_astronauts = sorted([x for x in available_astronauts], key=lambda x: x.oxygen, reverse=True)[0:5]
        if not available_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")
        for i in range(len(available_astronauts)):
            astronauts_in_open_space += 1
            astronaut = available_astronauts[i]
            while astronaut.oxygen > 0:
                if planet.items:
                    astronaut.backpack.append(planet.items.pop())
                    astronaut.breathe()
                else:
                    self.successful_missions += 1
                    return f'Planet: {planet_name} was explored. {astronauts_in_open_space} ' \
                           f'astronauts participated in collecting items.'
        self.unsuccessful_missions += 1
        return f'Mission is not completed.'

    def report(self):
        res = ''
        res += f"{self.successful_missions} successful missions!" \
               f"\n{self.unsuccessful_missions} missions were not completed!"
        astronauts = [a for a in self.astronaut_repository.astronauts]
        if astronauts:
            res += "\nAstronauts' info:"
            for a in astronauts:
                res += f"\nName: {a.name}"
                res += f"\nOxygen: {a.oxygen}"
                if a.backpack:
                    res += f"\nBackpack items: {', '.join(a.backpack)}"
                else:
                    res += '\nBackpack items: "none"'
        return res


# ll = [1, 2, 3, 4, 5, 6]
# available_astronauts = sorted(ll, key=lambda x: [0], reverse=True)[0:15]
# print(available_astronauts)
#
ss = SpaceStation()
ss.add_astronaut("Geodesist", "Ivan")
ss.add_astronaut("Meteorologist", "Van")
ss.add_planet("mars", "food, water, trees")
ss.add_planet("venera", "sun")
ss.add_planet("earth", "food, water, trees, food, water, trees, food, water, trees, food, water, trees, food, water, trees")
ss.send_on_mission("mars")
ss.send_on_mission("venera")
ss.send_on_mission("earth")


print(ss.report())
