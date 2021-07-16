class Equipment:
    _current_id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Equipment._current_id
        Equipment._current_id += 1

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Equipment._current_id
