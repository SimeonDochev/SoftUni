class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)
 
    def get_data(self):
        return self.__data
 
    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()
 
    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a
 
    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]
 
    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")
 
        self.get_data().insert(index, el)
 
    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]
 
    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class IntegerListTests(TestCase):
    def setUp(self) -> None:
        self.il = IntegerList(5, 6, 7)

    def test_initialization_with_valid_numbers(self):
        self.assertEqual([5, 6, 7], self.il._IntegerList__data)

    def test_initialization_with_invalid_elements(self):
        test_list = IntegerList(5, 5.5, 6)
        actual_result = test_list._IntegerList__data
        self.assertEqual([5, 6], actual_result)

    def test_add_operation_valid(self):
        expected = self.il.add(8)
        self.assertEqual([5, 6, 7, 8], expected)

    def test_add_operation_invalid_type(self):
        with self.assertRaises(ValueError):
            self.il.add(5.5)

    def test_remove_index_operation_valid(self):
        removed_element = self.il.remove_index(0)
        self.assertEqual(5, removed_element)
        self.assertEqual([6, 7], self.il._IntegerList__data)

    def test_remove_index_operation_invalid_index(self):
        with self.assertRaises(IndexError):
            self.il.remove_index(5)

    def test_get_operation_valid(self):
        actual_result = self.il.get(0)
        self.assertEqual(5, actual_result)

    def test_get_operation_invalid_index(self):
        with self.assertRaises(IndexError):
            self.il.get(5)

    def test_insert_operation_valid(self):
        self.il.insert(0, 4)
        self.assertEqual(4, self.il._IntegerList__data[0])

    def test_insert_operation_invalid_index(self):
        with self.assertRaises(IndexError):
            self.il.insert(5, 8)

    def test_insert_operation_invalid_type(self):
        with self.assertRaises(ValueError):
            self.il.insert(0, 5.5)

    def test_get_biggest(self):
        actual_result = self.il.get_biggest()
        self.assertEqual(7, actual_result)

    def test_get_index_valid(self):
        actual_result = self.il.get_index(5)
        self.assertEqual(0, actual_result)


if __name__ == "__main__":
    main()
