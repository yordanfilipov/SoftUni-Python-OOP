from project.plantation import Plantation

from unittest import TestCase, main


class TestPlantation(TestCase):
    def setUp(self):
        self.pl = Plantation(37)

    def test_init(self):
        size = 37

        self.assertEqual(size, self.pl.size)
        self.assertEqual({}, self.pl.plants)
        self.assertEqual([], self.pl.workers)

    def test_size_setter(self):
        new_size = -3
        exp = "Size must be positive number!"

        with self.assertRaises(ValueError) as context:
            self.pl.size = new_size

        self.assertEqual(exp, str(context.exception))

    def test_hire_worker_already_hired_raises(self):
        self.pl.workers = ['Ivan', 'Gosho']
        exp = 'Worker already hired!'

        with self.assertRaises(ValueError) as context:
            self.pl.hire_worker('Ivan')

        self.assertEqual(exp, str(context.exception))

    def test_hire_worker_not_hired(self):
        self.pl.workers = ['Ivan', 'Gosho']
        act = self.pl.hire_worker('Dimitar')
        exp = 'Dimitar successfully hired.'
        new_workers = ['Ivan', 'Gosho', 'Dimitar']

        self.assertEqual(exp, act)
        self.assertEqual(new_workers, self.pl.workers)

    def test_length(self):
        self.pl.plants = {"Ivan": ['1', '2', '5'], "Gosho": ['2', '3']}
        exp = 5
        act = self.pl.__len__()

        self.assertEqual(exp, act)

    def test_planting_worker_not_in_workers_raises(self):
        self.pl.workers = ['Ivan', 'Gosho']
        self.pl.plants = {"Ivan": ['rose', 'carrot'], "Gosho": ['tree', 'grass', 'apple']}
        exp = f'Worker with name Dimo is not hired!'

        with self.assertRaises(ValueError) as context:
            self.pl.planting('Dimo', 'rose')

        self.assertEqual(exp, str(context.exception))

    def test_planting_length_full_raises(self):
        self.pl.size = 5
        self.pl.workers = ['Ivan', 'Gosho']
        self.pl.plants = {"Ivan": ['rose', 'carrot'], "Gosho": ['tree', 'grass', 'apple']}
        exp = f'The plantation is full!'

        with self.assertRaises(ValueError) as context:
            self.pl.planting('Ivan', 'melon')

        self.assertEqual(exp, str(context.exception))

    def test_planting_worker_planting_a_plant(self):
        self.pl.workers = ['Ivan', 'Gosho']
        self.pl.plants = {"Ivan": ['rose', 'carrot'], "Gosho": ['tree', 'grass', 'apple']}
        exp = f'Ivan planted melon.'
        act = self.pl.planting('Ivan', 'melon')
        new_plants = {"Ivan": ['rose', 'carrot', 'melon'], "Gosho": ['tree', 'grass', 'apple']}

        self.assertEqual(exp, act)
        self.assertEqual(new_plants, self.pl.plants)

    def test_planting_worker_planting_first_plant(self):
        self.pl.workers = ['Ivan', 'Gosho']
        self.pl.plants = {"Ivan": ['rose', 'carrot'], "Gosho": ['tree', 'grass', 'apple']}
        self.pl.hire_worker("Dimitar")
        act = self.pl.planting('Dimitar', 'melon')
        exp = "Dimitar planted it's first melon."
        new_plants = {"Ivan": ['rose', 'carrot'], "Gosho": ['tree', 'grass', 'apple'], "Dimitar": ['melon']}
        self.assertEqual(exp, act)
        self.assertEqual(new_plants, self.pl.plants)

    def test_str(self):
        self.pl.workers = ['Ivan', 'Gosho']
        self.pl.plants = {"Ivan": ['rose', 'carrot'], "Gosho": ['tree', 'grass']}
        act = self.pl.__str__()
        exp = f'Plantation size: 37\n' \
              f'Ivan, Gosho\n' \
              f'Ivan planted: rose, carrot\n' \
              f'Gosho planted: tree, grass'
        self.assertEqual(exp, act)

    def test_repr(self):
        self.pl.workers = ['Ivan', 'Gosho']
        act = self.pl.__repr__()
        exp = f'Size: 37\n' \
              f'Workers: Ivan, Gosho'
        self.assertEqual(exp, act)


if __name__ == '__main__':
    main()
