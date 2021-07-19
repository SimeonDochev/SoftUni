def start_playing(obj):
    return obj.play()


class Children:
    def play(self):
        return "Children are playing"


piano = Children()
start_playing(piano)

