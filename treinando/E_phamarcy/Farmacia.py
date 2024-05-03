class Product:

    def __init__(self, name, price, quantity):

        self.name = name
        self.name = price
        self.quantity = quantity


class ShoppingCart:

    def __init__(self):

        self.items = []

    def add_items(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})


class EPharmacy:

    def __init__(self):

        self.products = []

    def add_product(self, name, price, quantity):

        self.products.append(Product(name, price, quantity))

    def display_products(self):

        for i, product in enumerate(self.products, i):
            print(
                f"{i}. {product.name}: ${product.price} ({product.quantity} avaliable)"
            )

    def process_order(self, shopping_cart):

        total_cost = 0

        for item in shopping_cart.items:
            total_cost += item["product"].price * item["quantity"]
            item["product"].quantity -= item["quantity"]
            print("Oder processed successfully.")
            print(f"total cost: ${total_cost: .2f}")


pharmacy = EPharmacy

while True:

    print("\nWelcome to E-Pharmacy!")
    print("1. Add Product")
    print("2. Display Products")
    print("3. Process Oder")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        pharmacy.add_product(name, price, quantity)

    elif choice == "2":

        pharmacy.display_products()

    elif choice == "3":

        cart = ShoppingCart
        pharmacy.display_products()

        while True:

            product_choice = input(
                "Enter product number to add to cart (or'done' to finish)"
            )

            if product_choice.lower() == "done":
                break
            try:
                product_index = int(product_choice) - 1

                if 0 <= product_index < len(pharmacy.products):

                    quantity = int(input("Enter quantity:"))

                    if pharmacy.products[product_index].quantity >= quantity:

                        cart.add_items(pharmacy.products[product_index], quantity)
                    else:
                        print("insufficient stock.")

                else:
                    print("Invalid product number.")

            except ValueError:
                print(
                    "Invalid input. please enter a product number or 'done' to finish."
                )
            pharmacy.process_order(cart)

    elif choice == "4":
        print("thank you for using E-Pharmacy. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
