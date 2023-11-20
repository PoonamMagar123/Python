class Database:
    invoices = []

    @classmethod
    def add_invoice(cls, invoice):
        cls.invoices.append(invoice)

    @classmethod
    def get_invoices(cls):
        return cls.invoices
