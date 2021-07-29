from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    _TYPE = "Heavy"
    _MEMORY_COEFFICIENT = 0.75
    _CAPACITY_COEFFICIENT = 2

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name,
                         HeavyHardware._TYPE,
                         int(capacity * HeavyHardware._CAPACITY_COEFFICIENT),
                         int(memory * HeavyHardware._MEMORY_COEFFICIENT))
