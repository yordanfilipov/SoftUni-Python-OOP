from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def test_init(self):
        mammal = Mammal("Ivan", "monkey", "coco")
        self.assertEqual(mammal.name, "Ivan")
        self.assertEqual(mammal.type, "monkey")
        self.assertEqual(mammal.sound, "coco")
        self.assertEqual(mammal._Mammal__kingdom, "animals")

    def test_make_sound(self):
        mammal = Mammal("Ivan", "monkey", "coco")
        result = mammal.make_sound()
        self.assertEqual(result, "Ivan makes coco")

    def test_get_kingdom(self):
        mammal = Mammal("Ivan", "monkey", "coco")
        result = mammal.get_kingdom()
        self.assertEqual(result, "animals")

    def test_info(self):
        mammal = Mammal("Ivan", "monkey", "coco")
        result = mammal.info()
        self.assertEqual(result, "Ivan is of type monkey")

if __name__ == "__main__":
    main()