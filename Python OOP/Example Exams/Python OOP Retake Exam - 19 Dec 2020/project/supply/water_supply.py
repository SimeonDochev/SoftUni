from project.supply.supply import Supply
from project.survivor import Survivor


class WaterSupply(Supply):
    _NEEDS_INCREASE = 40

    def __init__(self):
        super().__init__(WaterSupply._NEEDS_INCREASE)

    def apply(self, survivor: Survivor):
        survivor.needs += WaterSupply._NEEDS_INCREASE
