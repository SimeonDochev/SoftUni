class Trainer:
    _current_id = 1

    def __init__(self, name):
        self.name = name
        self.id = Trainer._current_id
        Trainer._current_id += 1

    @staticmethod
    def get_next_id():
        return Trainer._current_id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
