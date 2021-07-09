from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for prod in self.products:
            if prod.name == product_name:
                return prod

    def remove(self, product_name):
        for prod in self.products:
            if prod.name == product_name:
                self.products.remove(prod)

    def __repr__(self):
        result = ""

        for idx in range(len(self.products)):
            if not idx == len(self.products) - 1:
                result += f"{self.products[idx].name}: {self.products[idx].quantity}\n"
            else:
                result += f"{self.products[idx].name}: {self.products[idx].quantity}"
        return result
