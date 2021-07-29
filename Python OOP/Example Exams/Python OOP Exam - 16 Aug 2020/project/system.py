from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"
        hardware = hardware[0]
        try:
            hardware.install(ExpressSoftware(name, capacity_consumption, memory_consumption))
            System._software.append(hardware.software_components[-1])
        except Exception as e:
            return str(e)

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"
        hardware = hardware[0]
        try:
            hardware.install(LightSoftware(name, capacity_consumption, memory_consumption))
            System._software.append(hardware.software_components[-1])
        except Exception as e:
            return str(e)

    @staticmethod
    def release_software_component(hardware_name, software_name):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        software = [s for s in System._software if s.name == software_name]
        if not hardware or not software:
            return "Some of the components do not exist"
        hardware = hardware[0]
        software = software[0]
        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        total_memory = sum([h.memory for h in System._hardware])
        total_capacity = sum([h.capacity for h in System._hardware])
        total_memory_used = sum([h.used_memory for h in System._hardware])
        total_capacity_used = sum([h.used_capacity for h in System._hardware])

        result = f"System Analysis\n"
        result += f"Hardware Components: {len(System._hardware)}\n"
        result += f"Software Components: {len(System._software)}\n"
        result += f"Total Operational Memory: {total_memory_used} / {total_memory}\n"
        result += f"Total Capacity Taken: {total_capacity_used} / {total_capacity}"
        return result

    @staticmethod
    def system_split():
        result = []
        for hardware in System._hardware:
            current_result = f"Hardware Component - {hardware.name}\n"
            current_result += f"Express Software Components: " \
                              f"{len([s for s in hardware.software_components if s.__class__.__name__ == 'ExpressSoftware'])}\n"
            current_result += f"Light Software Components: " \
                              f"{len([s for s in hardware.software_components if s.__class__.__name__ == 'LightSoftware'])}\n"
            current_result += f"Memory Usage: {hardware.used_memory} / {hardware.memory}\n"
            current_result += f"Capacity Usage: {hardware.used_capacity} / {hardware.capacity}\n"
            current_result += f"Type: {hardware.type}\n"
            software_components_names = [s.name for s in hardware.software_components]
            current_result += f"Software Components: " \
                              f"{', '.join(software_components_names) if software_components_names else 'None'}"
            result.append(current_result)

        return ''.join(result)
