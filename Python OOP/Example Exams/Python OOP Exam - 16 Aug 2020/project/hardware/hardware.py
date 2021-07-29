from project.software.software import Software


class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    @property
    def used_memory(self):
        return sum([s.memory_consumption for s in self.software_components])

    @property
    def used_capacity(self):
        return sum([s.capacity_consumption for s in self.software_components])

    def install(self, software: Software):
        if not self.enough_memory(software.memory_consumption) or not self.enough_capacity(software.capacity_consumption):
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def enough_memory(self, memory):
        available_memory = self.memory - self.used_memory
        return True if available_memory >= memory else False

    def enough_capacity(self, capacity):
        available_capacity = self.capacity - self.used_capacity
        return True if available_capacity >= capacity else False

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)
