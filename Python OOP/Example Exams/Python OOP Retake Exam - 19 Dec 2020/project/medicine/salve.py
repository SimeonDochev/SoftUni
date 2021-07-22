from project.medicine.medicine import Medicine
from project.survivor import Survivor


class Salve(Medicine):
    _HEALTH_INCREASE = 50

    def __init__(self):
        super().__init__(Salve._HEALTH_INCREASE)

    def apply(self, survivor: Survivor):
        survivor.health += Salve._HEALTH_INCREASE
