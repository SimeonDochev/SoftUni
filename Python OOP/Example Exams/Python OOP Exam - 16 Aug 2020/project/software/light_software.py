from project.software.software import Software


class LightSoftware(Software):
    _TYPE = "Light"
    _CAPACITY_CONSUMPTION_COEFFICIENT = 1.5
    _MEMORY_CONSUMPTION_COEFFICIENT = 0.5

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name,
                         LightSoftware._TYPE,
                         int(capacity_consumption * LightSoftware._CAPACITY_CONSUMPTION_COEFFICIENT),
                         int(memory_consumption * LightSoftware._MEMORY_CONSUMPTION_COEFFICIENT))
