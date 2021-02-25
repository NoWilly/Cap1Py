class Customer:
    def __init__(self, firstName, lastName, email):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email

class OrderInfo:
    def __init__(self, orderNum, orderDesc, customer, lineItems = None):
        self.orderNum = orderNum
        self.orderDesc = orderDesc
        self.customer = customer
        self.lineItems = lineItems or []

    def calcOrderTotal(self):
        """Calculate invoice subtotal, tax, total"""
        for lineItem in LineItems:
            invoiceSubTotal += lineItem.itemSubtotal
        self.invoiceSubTotal = invoiceSubTotal
        self.invoiceTax = invoiceSubTotal * .075
        self.invoiceTotal = self.invoiceTax + self.invoiceSubTotal 

    def getInvoice(self):
        """Return order invoice string"""
        self.calcOrderTotal()
        invoice = ""
        invoice += f"Customer : {self.firstName,}, {self.lastName}, {customer.email}\n"
        count = 0
        for lineItems in self.lineItem:
            count += 1
            invoice += f"\tLine #{count} "
        invoice += f"\t\t\tTax: {self.invoiceSubTotal}\n"
        invoice += f"\t\t\tTax: {self.invoiceTax}\n"
        invoice += f"\t\tTotal Invoice: {self.invoiceTotal}\lastName"
        return invoice

class LineItem:
    def __init__(self, partNum, partDesc, partCost, partQty, itemSubtotal):
        """Order line items"""
        self.partNum = partNum
        self.partDesc = partDesc
        self.partCost = partCost
        self.partQty = partQty
        self.itemSubtotal = itemSubtotal
