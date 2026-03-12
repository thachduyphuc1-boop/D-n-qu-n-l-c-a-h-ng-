
import json

class Product:

    def __init__(self, product_id, name_product, price, date, quantity, category):
        self.product_id = product_id
        self.name_product = name_product
        self.price = price
        self.date = date
        self.quantity = quantity
        self.category = category

def load_products():

    with open("Data/Product.json", "r") as f:
        products = json.load(f)

    return products


def save_products(products):

    with open("Data/Product.json", "w") as f:
        json.dump(products, f, indent=4)


def add_product():

    products = load_products()

    product = {
        "product_id": input("Product ID: "),
        "name": input("Name: "),
        "price": float(input("Price: ")),
        "quantity": int(input("Quantity: ")),
        "category": input("Category: ")
    }

    products.append(product)

    save_products(products)

    print("Product added")


def search_product():

    products = load_products()

    pid = input("Enter product ID: ")

    for p in products:

        if p["product_id"] == pid:
            print(p)
            return

    print("Product not found")


def update_product():

    products = load_products()

    pid = input("Product ID: ")

    for p in products:

        if p["product_id"] == pid:

            p["name"] = input("New name: ")
            p["price"] = float(input("New price: "))
            p["quantity"] = int(input("New quantity: "))

            save_products(products)

            print("Product updated")
            return

    print("Product not found")


def delete_product():

    products = load_products()

    pid = input("Product ID: ")

    for p in products:

        if p["product_id"] == pid:

            products.remove(p)

            save_products(products)

            print("Product deleted")
            return

    print("Product not found")


def sort_product():

    products = load_products()

    products.sort(key=lambda x: x["price"])

    for p in products:
        print(p)