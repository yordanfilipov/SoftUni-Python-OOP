from abc import ABC, abstractmethod


class Supply(ABC):
    @abstractmethod
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name cannot be an empty string.")
        self.__name = value

    @property
    def energy(self):
        return self.__capacity

    @energy.setter
    def energy(self, value):
        if value < 0:
            raise ValueError("Energy cannot be less than zero.")
        self.__capacity = value

    def details(self):
        result = f"{self.__class__.__name__}: {self.name}, {self.energy}"
        return result


