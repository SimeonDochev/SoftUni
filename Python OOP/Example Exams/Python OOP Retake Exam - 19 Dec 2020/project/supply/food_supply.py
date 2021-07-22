from project.supply.supply import Supply
from project.survivor import Survivor


class FoodSupply(Supply):
    _NEEDS_INCREASE = 20

    def __init__(self):
        super().__init__(FoodSupply._NEEDS_INCREASE)

    def apply(self, survivor: Survivor):
        survivor.needs += FoodSupply._NEEDS_INCREASE
