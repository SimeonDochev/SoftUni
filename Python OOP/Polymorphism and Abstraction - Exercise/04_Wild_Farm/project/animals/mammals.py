from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    _LIKED_FOOD = [Vegetable, Fruit]
    _WEIGHT_INCREASE = 0.10

    @staticmethod
    def make_sound():
        return "Squeak"


class Dog(Mammal):
    _LIKED_FOOD = [Meat]
    _WEIGHT_INCREASE = 0.40

    @staticmethod
    def make_sound():
        return "Woof!"


class Cat(Mammal):
    _LIKED_FOOD = [Vegetable, Meat]
    _WEIGHT_INCREASE = 0.30

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):
    _LIKED_FOOD = [Meat]
    _WEIGHT_INCREASE = 1

    @staticmethod
    def make_sound():
        return "ROAR!!!"
