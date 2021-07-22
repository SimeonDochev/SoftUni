from project.medicine.medicine import Medicine
from project.survivor import Survivor


class Painkiller(Medicine):
    _HEALTH_INCREASE = 20

    def __init__(self):
        super().__init__(Painkiller._HEALTH_INCREASE)

    def apply(self, survivor: Survivor):
        survivor.health += Painkiller._HEALTH_INCREASE
