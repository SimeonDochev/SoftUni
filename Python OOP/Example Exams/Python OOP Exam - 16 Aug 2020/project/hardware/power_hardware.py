from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    _TYPE = "Power"
    _CAPACITY_COEFFICIENT = 0.25
    _MEMORY_COEFFICIENT = 1.75

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name,
                         PowerHardware._TYPE,
                         int(capacity * PowerHardware._CAPACITY_COEFFICIENT),
                         int(memory * PowerHardware._MEMORY_COEFFICIENT))
