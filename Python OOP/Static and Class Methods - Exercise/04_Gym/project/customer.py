class Customer:
    _current_id = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer._current_id
        Customer._current_id += 1

    @staticmethod
    def get_next_id():
        return Customer._current_id

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
