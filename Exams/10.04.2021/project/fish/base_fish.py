from abc import ABC, abstractmethod


class BaseFish(ABC):
    @abstractmethod
    def __init__(self, name, species, size, price):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__validate_price(value)
        self.__price = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        self.__validate_species(value)
        self.__species = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    @staticmethod
    def __validate_name(value):
        if not value:
            raise ValueError("Fish name cannot be an empty string.")

    @staticmethod
    def __validate_species(value):
        if not value:
            raise ValueError("Fish species cannot be an empty string.")

    @staticmethod
    def __validate_price(value):
        if value <= 0:
            raise ValueError("Price cannot be equal to or below zero.")

    @abstractmethod
    def eat(self):
        self.size += 5
