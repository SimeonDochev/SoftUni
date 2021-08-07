from unittest import TestCase, main

from project.people.child import Child
from project.rooms.room import Room


class RoomTests(TestCase):
    def setUp(self) -> None:
        self.room = Room("Test", 500, 2)

    def test_init(self):
        self.assertEqual("Test", self.room.family_name)
        self.assertEqual(500, self.room.budget)
        self.assertEqual(2, self.room.members_count)
        self.assertEqual([], self.room.children)
        self.assertEqual(0, self.room.expenses)

    def test_expenses_setter_with_valid_value(self):
        self.room.expenses = 20
        self.assertEqual(20, self.room.expenses)

    def test_expenses_setter_with_invalid_value_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -2
        expected_result = "Expenses cannot be negative"
        actual_result = str(ex.exception)
        self.assertEqual(expected_result, actual_result)

    def test_calculate_expenses(self):
        self.assertEqual(0, self.room.expenses)
        child = Child(5, 4, 1)
        self.room.calculate_expenses([child])
        self.assertEqual(300, self.room.expenses)


if __name__ == "__main__":
    main()
