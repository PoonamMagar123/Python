from invoices.invoice import Invoice

from clients.client import clients
from projects.project import Project
from utils.database import Database

def create_invoice():
    client_name = input("Enter client name: ")
    project_name = input("Enter project name: ")
    amount = float(input("Enter amount: "))
    
class Client:
    def __init__(self, name):
        self.name = name

    # Example list of clients
    clients = [Client("Client1"), Client("Client2"), Client("Client3")]
    # client = Client(client_name)
    project = Project(project_name)
    invoice = Invoice(client, project, amount)

    Database.add_invoice(invoice)
    print("Invoice created successfully.")

def display_invoices():
    invoices = Database.get_invoices()

    print("\nInvoices:")
    for index, invoice in enumerate(invoices, start=1):
        print(f"{index}. Client: {invoice.client.name}, Project: {invoice.project.name}, Amount: ${invoice.amount}")

def main():
    while True:
        print("\nConstruction Billing System")
        print("1. Create Invoice")
        print("2. Display Invoices")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_invoice()
        elif choice == '2':
            display_invoices()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
