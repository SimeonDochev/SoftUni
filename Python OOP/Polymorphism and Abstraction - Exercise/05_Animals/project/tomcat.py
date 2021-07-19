from project.cat import Cat


class Tomcat(Cat):
    _GENDER = "Male"
    _SOUND = "Hiss"

    def __init__(self, name, age):
        super().__init__(name, age, Tomcat._GENDER)

    @staticmethod
    def make_sound():
        return Tomcat._SOUND
