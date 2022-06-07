from project.pet_shop import PetShop
from unittest import TestCase, main


class TestPetShop(TestCase):

    def setUp(self) -> None:
        self.ps = PetShop("Shop")

    def test_correct_initialization(self):
        self.assertEqual("Shop", self.ps.name)
        self.assertEqual({}, self.ps.food)
        self.assertEqual([], self.ps.pets)

    def test_add_food_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.ps.add_food("food", -1.5)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

    def test_add_food_correct_return(self):
        result = self.ps.add_food("food", 2.2)
        self.assertEqual("Successfully added 2.20 grams of food.", result)

    def test_add_food_correct_calculations(self):
        self.assertEqual({}, self.ps.food)
        self.ps.add_food("food", 2.2)
        self.assertEqual({"food": 2.2}, self.ps.food)

    def test_add_pet_correct(self):
        self.ps.add_pet("Pesho")
        self.assertEqual(["Pesho"], self.ps.pets)

    def test_add_pet_correct_return(self):
        result = self.ps.add_pet("Pesho")
        self.assertEqual("Successfully added Pesho.", result)

    def test_add_pet_raises(self):
        self.ps.add_pet("Pesho")
        with self.assertRaises(Exception) as e:
            self.ps.add_pet("Pesho")
        self.assertEqual("Cannot add a pet with the same name", str(e.exception))

    def test_feed_pet_invalid_pet_name(self):
        self.ps.add_pet("Pesho")
        with self.assertRaises(Exception) as e:
            self.ps.feed_pet("food", "Ivan")
        self.assertEqual("Please insert a valid pet name", str(e.exception))

    def test_feed_pet_invalid_food_name(self):
        self.ps.add_pet("Pesho")
        self.ps.add_food("food", 2.2)
        result = self.ps.feed_pet("something", "Pesho")
        self.assertEqual("You do not have something", result)

    def test_feed_pet_adding_food_case(self):
        self.ps.add_food("food", 2.2)
        self.ps.add_pet("Pesho")
        result = self.ps.feed_pet("food", "Pesho")
        self.assertEqual("Adding food...", result)

    def test_feed_pet_added_food(self):
        self.ps.add_food("food", 2.2)
        self.ps.add_pet("Pesho")
        self.ps.feed_pet("food", "Pesho")
        self.assertEqual({"food": 1002.2}, self.ps.food)

    def test_feed_pet_correct_return(self):
        self.ps.add_pet("Pesho")
        self.ps.add_food("food", 101)
        result = self.ps.feed_pet("food", "Pesho")
        self.assertEqual("Pesho was successfully fed", result)

    def test_feed_pet_correct_quantities_left(self):
        self.ps.add_pet("Pesho")
        self.ps.add_food("food", 101)
        self.ps.feed_pet("food", "Pesho")
        self.assertEqual({"food": 1}, self.ps.food)

    def test_repr(self):
        self.ps.add_pet("Pesho")
        self.ps.add_pet("Ivan")
        expected = "Shop Shop:\nPets: Pesho, Ivan"
        result = repr(self.ps)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()

