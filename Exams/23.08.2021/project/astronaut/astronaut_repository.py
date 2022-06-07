from project.astronaut.astronaut import Astronaut
from project.astronaut.biologist import Biologist
from project.astronaut.meteorologist import Meteorologist


class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        if astronaut in self.astronauts:
            self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        found_astronaut = [a for a in self.astronauts if a.name == name]
        if found_astronaut:
            found_astronaut = found_astronaut[0]
            return found_astronaut
