from unittest import TestCase, main
from project.factory.paint_factory import PaintFactory


class PaintFactoryTests(TestCase):
    def setUp(self) -> None:
        self.pfactory = PaintFactory("Test", 10)

    def test_init_method(self):
        self.assertEqual("Test", self.pfactory.name)
        self.assertEqual(10, self.pfactory.capacity)
        self.assertEqual({}, self.pfactory.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.pfactory.valid_ingredients)
        self.assertEqual({}, self.pfactory.ingredients)

    def test_can_add(self):
        self.assertTrue(self.pfactory.can_add(5))
        self.assertFalse(self.pfactory.can_add(11))

    def test_add_valid_ingredient(self):
        self.assertEqual({}, self.pfactory.ingredients)
        self.pfactory.add_ingredient("white", 1)
        self.assertEqual({"white": 1}, self.pfactory.ingredients)

    def test_add_invalid_ingredient_raises(self):
        with self.assertRaises(TypeError) as ex:
            self.pfactory.add_ingredient("test", 5)
        expected_result = "Ingredient of type test not allowed in PaintFactory"
        actual_result = str(ex.exception)
        self.assertEqual(expected_result, actual_result)

    def test_add_invalid_quantity_ingredient_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.pfactory.add_ingredient("white", 11)
        expected_result = "Not enough space in factory"
        actual_result = str(ex.exception)
        self.assertEqual(expected_result, actual_result)

    def test_remove_valid_ingredient_quantity(self):
        self.pfactory.ingredients = {"white": 5}
        self.pfactory.remove_ingredient("white", 4)
        self.assertEqual({"white": 1}, self.pfactory.ingredients)

    def test_remove_invalid_ingredient_raises(self):
        with self.assertRaises(KeyError) as ex:
            self.pfactory.remove_ingredient("white", 5)
        expected_result = "'No such ingredient in the factory'"
        actual_result = str(ex.exception)
        self.assertEqual(expected_result, actual_result)

    def test_remove_invalid_ingredient_quantity_raises(self):
        self.pfactory.ingredients = {"white": 5}
        with self.assertRaises(ValueError) as ex:
            self.pfactory.remove_ingredient("white", 6)
        expected_result = "Ingredients quantity cannot be less than zero"
        actual_result = str(ex.exception)
        self.assertEqual(expected_result, actual_result)

    def test_repr(self):
        self.pfactory.ingredients = {"white": 5, "yellow": 2}
        expected_result = "Factory name: Test with capacity 10.\n" \
                          "white: 5\n" \
                          "yellow: 2\n"
        actual_result = repr(self.pfactory)
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    main()
