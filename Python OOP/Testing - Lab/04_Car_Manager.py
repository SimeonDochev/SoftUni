class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0
    
    @property
    def make(self):
        return self.__make
    
    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption
    
    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity
    
    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount
    
    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


from unittest import TestCase, main


class CarManagerTests(TestCase):
    def setUp(self) -> None:
        self.car = Car("BMW", "E90", 5.5, 60)

    def test_car_init_valid(self):
        self.assertEqual("BMW", self.car.make)
        self.assertEqual("E90", self.car.model)
        self.assertEqual(5.5, self.car.fuel_consumption)
        self.assertEqual(60, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_car_init_invalid_make_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car("", "test", 5, 60)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_car_init_invalid_model_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car("test", "", 5, 60)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_car_init_invalid_fuel_consumption_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car("test", "test", 0, 60)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_car_init_invalid_fuel_capacity_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car("test", "test", 5, 0)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_car_fuel_amount_invalid_raises(self):
        car = Car("test", "test", 5, 60)
        with self.assertRaises(Exception) as ex:
            car.fuel_amount = -10
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_car_fuel_increases_after_refueling(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

    def test_car_refueling_with_negative_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_car_fuel_decreases_after_driving(self):
        self.car.refuel(50)
        self.car.drive(130)
        self.assertEqual(42.85, self.car.fuel_amount)

    def test_driving_car_with_not_enough_fuel_raises(self):
        self.car.refuel(5)
        with self.assertRaises(Exception) as ex:
            self.car.drive(130)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    main()
