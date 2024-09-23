class Policyholder:
    def __init__(self, policyholder_id, name, status="Active"):
        self.policyholder_id = policyholder_id
        self.name = name
        self.status = status
        self.paid_products = []

    def register_policyholder(self):
        print(f"Policyholder {self.name} (ID: {self.policyholder_id}) registered.")

    def suspend_policyholder(self):
        self.status = "Suspended"
        print(f"Policyholder {self.name} has been suspended.")

    def reactivate_policyholder(self):
        self.status = "Active"
        print(f"Policyholder {self.name} has been reactivated.")

    def add_paid_product(self, product):
        self.paid_products.append(product)

    def display_details(self):
        products_list = ', '.join([product.name for product in self.paid_products])
        print(f"Policyholder: {self.name} (ID: {self.policyholder_id}) - Status: {self.status}")
        print(f"Paid Products: {products_list if products_list else 'None'}")
