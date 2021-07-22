from project.medicine.medicine import Medicine
from project.medicine.salve import Salve
from project.supply.food_supply import FoodSupply
from project.supply.supply import Supply
from project.supply.water_supply import WaterSupply
from project.medicine.painkiller import Painkiller
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors: list = []
        self.supplies: list = []
        self.medicine: list = []

    @property
    def food(self):
        food = [s for s in self.supplies if isinstance(s, FoodSupply)]
        if not food:
            raise IndexError("There are no food supplies left!")
        return food

    @property
    def water(self):
        water = [s for s in self.supplies if isinstance(s, WaterSupply)]
        if not water:
            raise IndexError("There are no water supplies left!")
        return water

    @property
    def painkillers(self):
        painkillers = [m for m in self.medicine if isinstance(m, Painkiller)]
        if not painkillers:
            raise IndexError("There are no painkillers left!")
        return painkillers

    @property
    def salves(self):
        salves = [m for m in self.medicine if isinstance(m, Salve)]
        if not salves:
            raise IndexError("There are no salves left!")
        return salves

    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        if survivor.needs_healing:
            medicine = None
            for med in self.medicine:
                if med.__class__.__name__ == medicine_type:
                    medicine = med
            medicine.apply(survivor)
            self.medicine.remove(medicine)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            sustenance = None
            for sus in self.supplies:
                if sus.__class__.__name__ == sustenance_type:
                    sustenance = sus
            sustenance.apply(survivor)
            self.supplies.remove(sustenance)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
        for survivor in self.survivors:
            food_supply = self.food[0]
            water_supply = self.water[0]
            food_supply.apply(survivor)
            water_supply.apply(survivor)
            self.supplies.remove(food_supply)
            self.supplies.remove(water_supply)
