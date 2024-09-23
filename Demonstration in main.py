from policyholder import Policyholder
from product import Product
from payment import Payment

# Create policyholders
policyholder1 = Policyholder(101, "Alice")
policyholder2 = Policyholder(102, "Bob")

# Register policyholders
policyholder1.register_policyholder()
policyholder2.register_policyholder()

# Create products
product1 = Product(201, "Health Insurance", 500)
product2 = Product(202, "Car Insurance", 300)

product1.create_product()
product2.create_product()

# Process payments
payment1 = Payment(policyholder1, product1, 500)
payment2 = Payment(policyholder2, product2, 300)

payment1.process_payment()
payment2.process_payment()

# Display policyholder details
policyholder1.display_details()
policyholder2.display_details()

# Suspend a policyholder
policyholder1.suspend_policyholder()

# Reactivate policyholder
policyholder1.reactivate_policyholder()

# Update product
product1.update_product(price=550)

# Suspend a product
product2.remove_product()

# Send payment reminder and apply penalty
payment1.send_reminder()
payment2.apply_penalty()
