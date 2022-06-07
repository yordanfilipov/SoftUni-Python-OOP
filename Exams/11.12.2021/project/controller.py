from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        car = [c for c in self.cars if c.model == model]
        if car:
            raise Exception(f"Car {model} is already created!")
        if car_type == "SportsCar" or car_type == "MuscleCar":
            if car_type == "SportsCar":
                car = SportsCar(model, speed_limit)
            else:
                car = MuscleCar(model, speed_limit)
            self.cars.append(car)
            return f'{car_type} {model} is created.'

    def create_driver(self, driver_name: str):
        driver = [d for d in self.drivers if d.name == driver_name]
        if driver:
            raise Exception(f"Driver {driver_name} is already created!")
        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f'Driver {driver_name} is created.'

    def create_race(self, race_name: str):
        race = [r for r in self.races if r.name == race_name]
        if race:
            raise Exception(f"Race {race_name} is already created!")
        race = Race(race_name)
        self.races.append(race)
        return f'Race {race_name} is created.'

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = [d for d in self.drivers if d.name == driver_name][0]
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        for i in range(len(self.cars) - 1, -1, -1):
            if type(self.cars[i]).__name__ == car_type and self.cars[i].is_taken == False:
                if not driver.car:
                    car = self.cars[i]
                    driver.car = car
                    car.is_taken = True
                    return f'Driver {driver_name} chose the car {car.model}.'
                else:
                    old_model = driver.car.model
                    driver.car.is_taken = False
                    car = self.cars[i]
                    driver.car = car
                    new_model = driver.car.model
                    car.is_taken = True
                    return f'Driver {driver_name} changed his car from {old_model} to {new_model}.'
        return f"Car {car_type} could not be found!"

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = [r for r in self.races if r.name == race_name][0]
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        driver = [d for d in self.drivers if d.name == driver_name][0]
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver in race.drivers:
            return f'Driver {driver_name} is already added in {race_name} race.'
        if race and driver and driver.car:
            race.drivers.append(driver)
            return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = [r for r in self.races if r.name == race_name][0]
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        drivers = [d for d in race.drivers]
        sorted_drivers = sorted(drivers, key=lambda x: x.car.speed_limit, reverse=True)
        result = []
        for i in range(3):
            i = sorted_drivers[i]
            i.number_of_wins += 1
            result.append(f'Driver {i.name} wins the {race_name} race with a speed of {i.car.speed_limit}.')
        return '\n'.join(result)


controller = Controller()
print(controller.create_driver("Peter"))
print(controller.create_car("SportsCar", "Porsche 718 Boxster", 470))
print(controller.add_car_to_driver("Peter", "SportsCar"))
print(controller.create_car("SportsCar", "Porsche 911", 580))
print(controller.add_car_to_driver("Peter", "SportsCar"))
print(controller.create_car("MuscleCar", "BMW ALPINA B7", 290))
print(controller.create_car("MuscleCar", "Mercedes-Benz AMG GLA 45", 420))
print(controller.create_driver("John"))
print(controller.create_driver("Jack"))
print(controller.create_driver("Kelly"))
print(controller.add_car_to_driver("Kelly", "MuscleCar"))
print(controller.add_car_to_driver("Jack", "MuscleCar"))
print(controller.add_car_to_driver("John", "SportsCar"))
print(controller.create_race("Christmas Top Racers"))
print(controller.add_driver_to_race("Christmas Top Racers", "John"))
print(controller.add_driver_to_race("Christmas Top Racers", "Jack"))
print(controller.add_driver_to_race("Christmas Top Racers", "Kelly"))
print(controller.add_driver_to_race("Christmas Top Racers", "Peter"))
print(controller.start_race("Christmas Top Racers"))
[print(d.name, d.number_of_wins) for d in controller.drivers]
