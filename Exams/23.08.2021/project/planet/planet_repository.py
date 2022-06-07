from project.planet.planet import Planet


class PlanetRepository:
    def __init__(self):
        self.planets = []  # an empty list of planets

    def add(self, planet: Planet):
        self.planets.append(planet)

    def remove(self, planet: Planet):
        if planet in self.planets:
            self.planets.remove(planet)

    def find_by_name(self, name: str):
        found_planet = [p for p in self.planets if p.name == name]
        if found_planet:
            found_planet = found_planet[0]
            return found_planet
