from project.animals.animal import Bird
from project.food import Vegetable, Fruit, Meat, Seed


class Owl(Bird):
    _LIKED_FOOD = [Meat]
    _WEIGHT_INCREASE = 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):
    _LIKED_FOOD = [Vegetable, Fruit, Meat, Seed]
    _WEIGHT_INCREASE = 0.35

    @staticmethod
    def make_sound():
        return "Cluck"
