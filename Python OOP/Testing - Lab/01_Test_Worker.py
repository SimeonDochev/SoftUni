class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTests(TestCase):
    def setUp(self) -> None:
        self.worker = Worker("Test", 500, 10)

    def test_worker_initialization(self):
        self.assertEqual("Test", self.worker.name)
        self.assertEqual(500, self.worker.salary)
        self.assertEqual(10, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_worker_energy_is_incremented_after_resting(self):
        self.assertEqual(10, self.worker.energy)
        self.worker.rest()
        self.assertEqual(11, self.worker.energy)

    def test_worker_tries_to_work_with_negative_energy_raises(self):
        worker = Worker("Test", 500, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_worker_salary_is_increased_after_working(self):
        self.assertEqual(0, self.worker.money)
        self.worker.work()
        self.assertEqual(500, self.worker.money)

    def test_worker_energy_is_decreased_after_working(self):
        self.assertEqual(10, self.worker.energy)
        self.worker.work()
        self.assertEqual(9, self.worker.energy)

    def test_get_info(self):
        expected = "Test has saved 0 money."
        actual = self.worker.get_info()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
