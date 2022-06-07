from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.v = Vehicle(55, 110)

    def test_init(self):
        fuel = 55
        hp = 110
        default_fc = 1.25
        vehicle = Vehicle(fuel, hp)
        self.assertEqual(vehicle.fuel, fuel)
        self.assertEqual(vehicle.horse_power, 110)
        self.assertEqual(vehicle.capacity, fuel)
        self.assertEqual(vehicle.fuel_consumption, default_fc)

    def test_drive(self):
        km = 20
        remaining_fuel = 30
        self.v.drive(km)
        self.assertEqual(self.v.fuel, remaining_fuel)

    def test_drive_exception(self):
        km = 100
        with self.assertRaises(Exception) as e:
            self.v.drive(km)
        self.assertEqual("Not enough fuel", str(e.exception))

    def test_refuel(self):
        self.v.fuel -= 20
        self.v.refuel(10)
        self.assertEqual(self.v.fuel, 45)

    def test_refuel_exception(self):
        with self.assertRaises(Exception) as e:
            self.v.refuel(5)
        self.assertEqual("Too much fuel", str(e.exception))

    def test_str(self):
        self.assertEqual(str(self.v),
                         "The vehicle has 110 horse power with 55 fuel left and 1.25 fuel consumption")


if __name__ == "__main__":
    main()
