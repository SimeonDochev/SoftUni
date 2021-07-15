from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.DVD_CAPACITY:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        current_customer = [customer for customer in self.customers if customer.id == customer_id][0]
        current_dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]
        if current_dvd in current_customer.rented_dvds:
            return f"{current_customer.name} has already rented {current_dvd.name}"
        if current_dvd.is_rented:
            return "DVD is already rented"
        if current_customer.age < current_dvd.age_restriction:
            return f"{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie"
        current_customer.rented_dvds.append(current_dvd)
        current_dvd.is_rented = True
        return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        current_customer = [customer for customer in self.customers if customer.id == customer_id][0]
        current_dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]
        if current_dvd in current_customer.rented_dvds:
            current_customer.rented_dvds.remove(current_dvd)
            current_dvd.is_rented = False
            return f"{current_customer.name} has successfully returned {current_dvd.name}"
        return f"{current_customer.name} does not have that DVD"

    def __repr__(self):
        result = []
        for customer in self.customers:
            result.append(repr(customer))
        for dvd in self.dvds:
            result.append(repr(dvd))
        return '\n'.join(result)
