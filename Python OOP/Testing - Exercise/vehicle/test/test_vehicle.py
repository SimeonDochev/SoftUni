from unittest import TestCase, main
from project.vehicle import Vehicle


class VehicleTests(TestCase):
    def setUp(self) -> None:
        self.car = Vehicle(60.5, 143)

    def test_vehicle_init(self):
        self.assertEqual(60.5, self.car.fuel)
        self.assertEqual(60.5, self.car.capacity)
        self.assertEqual(143, self.car.horse_power)
        self.assertEqual(1.25, self.car.fuel_consumption)

    def test_vehicle_fuel_decreases_after_driving(self):
        self.assertEqual(60.5, self.car.fuel)
        self.car.drive(40)
        self.assertEqual(10.5, self.car.fuel)

    def test_vehicle_drive_not_enough_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_vehicle_fuel_increases_after_refueling(self):
        self.car.fuel = 50
        self.car.refuel(10)
        self.assertEqual(60, self.car.fuel)

    def test_vehicle_refuel_too_much_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_vehicle_str_method(self):
        expected_result = "The vehicle has 143 horse power with 60.5 fuel left and 1.25 fuel consumption"
        actual_result = str(self.car)
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    main()
