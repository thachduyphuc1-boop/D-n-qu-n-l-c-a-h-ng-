
import json

class Customer:

    def __init__(self, id_customer, name_customer, phone_number, date):
        self.id_customer = id_customer
        self.name_customer = name_customer
        self.phone_number = phone_number
        self.date = date
        
def load_customers():

    with open("Data/Customer.json", "r") as f:
        customers = json.load(f)

    return customers


def save_customers(customers):

    with open("Data/Customer.json", "w") as f:
        json.dump(customers, f, indent=4)


def add_customer():

    customers = load_customers()

    customer = {
        "id": input("Customer ID: "),
        "name": input("Customer name: "),
        "phone": input("Phone number: ")
    }

    customers.append(customer)

    save_customers(customers)

    print("Customer added")


def search_customer():

    customers = load_customers()

    cid = input("Customer ID: ")

    for c in customers:

        if c["id"] == cid:
            print(c)
            return

    print("Customer not found")


def purchase_history():

    cid = input("Customer ID: ")

    with open("Data/Invoice.json", "r") as f:
        invoices = json.load(f)

    for inv in invoices:

        if inv["customer_id"] == cid:
            print(inv)