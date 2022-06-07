from project.pet_shop import PetShop

from unittest import TestCase, main


class TestPetShop(TestCase):
    def setUp(self):
        self.ps = PetShop("Cats")

    def test_init(self):
        self.assertEqual("Cats", self.ps.name)
        self.assertEqual({}, self.ps.food)
        self.assertEqual([], self.ps.pets)

    def test_add_food_less_or_equal_to_zero_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.ps.add_food("meat", 0)
        self.assertEqual("Quantity cannot be equal to or less than 0", str(ve.exception))

    def test_add_food_if_not_exists_in_list(self):
        result = self.ps.add_food("fish", 3)
        self.assertEqual("Successfully added 3.00 grams of fish.", result)

    def test_add_food_if_exists_in_list(self):
        self.ps.food = {"meat": 2}
        result = self.ps.add_food("meat", 3)
        self.assertEqual("Successfully added 3.00 grams of meat.", result)

    '''TO CHECK'''
    def test_add_food_correct_calculations(self):
        self.assertEqual({}, self.ps.food)
        self.ps.add_food("food", 2.2)
        self.assertEqual({"food": 2.2}, self.ps.food)
    '''TO CHECK'''

    def test_add_pet_if_exist_in_list_raises(self):
        self.ps.pets = ["cat", "dog"]
        with self.assertRaises(Exception) as e:
            self.ps.add_pet("dog")
        self.assertEqual("Cannot add a pet with the same name", str(e.exception))

    '''TO CHECK'''
    def test_add_pet_correct(self):
        self.ps.add_pet("Pesho")
        self.assertEqual(["Pesho"], self.ps.pets)
    '''TO CHECK'''

    def test_add_pet(self):
        self.ps.pets = ["cat", "dog"]
        result = self.ps.add_pet("mouse")
        self.assertEqual("Successfully added mouse.", result)

    def test_feed_pet_if_not_exist_in_list_raises(self):
        self.ps.pets = ["cat", "dog"]
        self.ps.food = {"fish": 2}
        with self.assertRaises(Exception) as e:
            self.ps.feed_pet("fish", "mouse")
        self.assertEqual("Please insert a valid pet name", str(e.exception))

    def test_feed_pet_if_food_not_exist_in_list(self):
        self.ps.food = {"meat": 2}
        self.ps.pets = ["cat", "dog"]
        result = self.ps.feed_pet("fish", "cat")
        self.assertEqual("You do not have fish", result)

    def test_feed_pet_if_food_is_less_than_one_hundred(self):
        self.ps.pets = ["cat", "dog"]
        self.ps.food = {"meat": 2}
        result = self.ps.feed_pet("meat", "cat")
        self.assertEqual("Adding food...", result)
    '''TO CHECK'''
    def test_feed_pet_added_food(self):
        self.ps.add_food("food", 2.2)
        self.ps.add_pet("Pesho")
        self.ps.feed_pet("food", "Pesho")
        self.assertEqual({"food": 1002.2}, self.ps.food)
    '''TO CHECK'''

    def test_feed_pet_if_food_is_enough(self):
        self.ps.pets = ["cat", "dog"]
        self.ps.food = {"meat": 101}
        result = self.ps.feed_pet("meat", "cat")
        self.assertEqual("cat was successfully fed", result)

    '''TO CHECK'''
    def test_feed_pet_correct_quantities_left(self):
        self.ps.add_pet("Pesho")
        self.ps.add_food("food", 101)
        self.ps.feed_pet("food", "Pesho")
        self.assertEqual({"food": 1}, self.ps.food)
    '''TO CHECK'''

    # def test_repr(self):
    #     self.ps.pets = ["cat", "dog"]
    #     result = f'Shop {self.ps.name}:\n' \
    #              f'Pets: {", ".join(self.ps.pets)}'
    #     self.assertEqual("Shop Cats:\nPets: cat, dog", result)

    def test_repr(self):
        self.ps.add_pet("Pesho")
        self.ps.add_pet("Ivan")
        expected = "Shop Cats:\nPets: Pesho, Ivan"
        result = repr(self.ps)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
