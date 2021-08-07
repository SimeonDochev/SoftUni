from unittest import TestCase, main
from project.hardware.hardware import Hardware
from project.software.software import Software


class HardwareTests(TestCase):
    def setUp(self) -> None:
        self.hw = Hardware("Test", "test", 100, 50)

    def test_init(self):
        self.assertEqual("Test", self.hw.name)
        self.assertEqual("test", self.hw.type)
        self.assertEqual(100, self.hw.capacity)
        self.assertEqual(50, self.hw.memory)
        self.assertEqual([], self.hw.software_components)

    def test_install_valid(self):
        software = Software("Software", "test", 20, 20)
        self.hw.install(software)
        self.assertEqual([software], self.hw.software_components)

    def test_install_not_enough_capacity_raises(self):
        software = Software("software", "test", 110, 20)
        with self.assertRaises(Exception) as ex:
            self.hw.install(software)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_install_not_enough_memory_raises(self):
        software = Software("software", "test", 50, 60)
        with self.assertRaises(Exception) as ex:
            self.hw.install(software)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_uninstall_software_valid(self):
        software = Software("Software", "test", 20, 20)
        self.hw.software_components = [software]
        self.hw.uninstall(software)
        self.assertEqual([], self.hw.software_components)


if __name__ == "__main__":
    main()
