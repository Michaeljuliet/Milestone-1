class Payment:
    def __init__(self, policyholder, product, amount):
        self.policyholder = policyholder
        self.product = product
        self.amount = amount

    def process_payment(self):
        print(f"Processing payment of ${self.amount} for {self.policyholder.name} on product {self.product.name}.")
        self.policyholder.add_paid_product(self.product)

    def send_reminder(self):
        print(f"Reminder: Payment for {self.product.name} is due for {self.policyholder.name}.")

    def apply_penalty(self):
        penalty = 10  # Assuming a fixed penalty amount
        print(f"A penalty of ${penalty} has been applied for {self.policyholder.name}.")
