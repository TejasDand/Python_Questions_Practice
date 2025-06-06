# Use keyword and positional arguments in a function.

def generate_bill(customer_name, product, price, quantity = 1):
    total = price * quantity

    print("-" * 30)

    print(f"Customer Name: {customer_name}")
    print(f"Product: {product}")
    print(f"Price per item: {price}")
    print(f"Quantity: {quantity}")
    print(f"Final amount to pay: {total}")

    print("-" * 30)

generate_bill("Rahul", "Bag", price=800, quantity=2)
generate_bill("Anita", "Fridge", price=15000)