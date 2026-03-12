
import json
from datetime import datetime

class Invoice:

    def __init__(self, id_invoice, invoice_date_make, staff_make, invoice_status, invoice_total):
        self.id_invoice = id_invoice
        self.invoice_date_make = invoice_date_make
        self.staff_make = staff_make
        self.invoice_status = invoice_status
        self.invoice_total = invoice_total

def load_invoices():

    with open("Data/Invoice.json", "r") as f:
        invoices = json.load(f)

    return invoices


def save_invoices(invoices):

    with open("Data/Invoice.json", "w") as f:
        json.dump(invoices, f, indent=4)


def calculate_total(items):

    total = 0

    for item in items:

        total += item["price"] * item["quantity"]

    return total


def create_invoice():

    invoices = load_invoices()

    invoice = {
        "invoice_id": input("Invoice ID: "),
        "date": str(datetime.now()),
        "customer_id": input("Customer ID: "),
        "items": [],
        "total": 0
    }

    while True:

        pid = input("Product ID (0 to stop): ")

        if pid == "0":
            break

        price = float(input("Price: "))
        quantity = int(input("Quantity: "))

        item = {
            "product_id": pid,
            "price": price,
            "quantity": quantity
        }

        invoice["items"].append(item)

    invoice["total"] = calculate_total(invoice["items"])

    invoices.append(invoice)

    save_invoices(invoices)

    print("Invoice created")


def view_invoice():

    invoices = load_invoices()

    iid = input("Invoice ID: ")

    for inv in invoices:

        if inv["invoice_id"] == iid:
            print(inv)
            return

    print("Invoice not found")