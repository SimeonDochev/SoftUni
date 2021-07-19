from project.cat import Cat


class Kitten(Cat):
    _GENDER = "Female"
    _SOUND = "Meow"

    def __init__(self, name, age):
        super().__init__(name, age, Kitten._GENDER)

    @staticmethod
    def make_sound():
        return Kitten._SOUND
