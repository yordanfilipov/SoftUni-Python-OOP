from project.train.train import Train

from unittest import TestCase, main


class TestTrain(TestCase):
    def setUp(self):
        self.tr = Train("Chaika", 5)
        self.tr.passengers = []

    def test_init(self):
        self.assertEqual("Chaika", self.tr.name)
        self.assertEqual(5, self.tr.capacity)
        self.assertEqual([], self.tr.passengers)

    def test_add_passenger_raises_len(self):
        self.tr.passengers = [1, 2, 3, 4, 5]
        with self.assertRaises(ValueError) as ve:
            self.tr.add(self.tr.name)
        self.assertEqual(self.tr.__class__.TRAIN_FULL, str(ve.exception))

    def test_add_passenger_raises_name(self):
        self.tr.passengers = ["Ivan", "Gosho"]
        with self.assertRaises(ValueError) as ve:
            self.tr.add("Ivan")
        self.assertEqual('Passenger Ivan Exists', str(ve.exception))

    def test_add_passenger(self):
        self.tr.passengers = ["Ivan", "Gosho"]
        result = self.tr.add("Petar")
        self.assertEqual("Added passenger Petar", result)

    def test_remove_passenger_raises(self):
        self.tr.passengers = ["Ivan", "Gosho"]
        with self.assertRaises(ValueError) as ve:
            self.tr.remove("Petar")
        self.assertEqual('Passenger Not Found', str(ve.exception))

    def test_remove_passenger(self):
        self.tr.passengers = ["Ivan", "Gosho"]
        result = self.tr.remove("Ivan")
        self.assertEqual("Removed Ivan", result)


if __name__ == '__main__':
    main()
