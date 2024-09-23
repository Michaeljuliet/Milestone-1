class Product:
    def __init__(self, product_id, name, price, status="Available"):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.status = status

    def create_product(self):
        print(f"Product '{self.name}' created.")

    def update_product(self, name=None, price=None):
        if name:
            self.name = name
        if price:
            self.price = price
        print(f"Product '{self.product_id}' updated.")

    def remove_product(self):
        self.status = "Suspended"
        print(f"Product '{self.name}' has been suspended.")
