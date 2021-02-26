from orderClasses import Customer, OrderInfo, LineItem

class Program:
    def main(self):
        """ Application starting point """
        print("Order processing application")
        customer = self.getCustomerInfo()
        order = self.getOrder()

        # Output invoice
        invoice = self.getInvoice(customer, order)
        print("\nCustomer Invoice\n")
        print(invoice)

    def getCustomerInfo(self):
        print("\tCustomer information")
        firstName = input("\t\tEnter first name: ")
        lastName = input("\t\tEnter last name: ")
        email = input("\t\tEnter email address: ")
        return Customer(firstName, lastName, email)
    
    def getOrder(self):
        print("\n\tCreate order:")
        order = []
        orderNum = input("\t\tEnter order number: ")
        orderDesc = input("\t\tEnter order description: ")
        order.append(OrderInfo(orderNum, orderDesc))
        noItems = int(input("\t\tHow many items are you ordering? "))
        count = 1
        print("\n\tEnter order details")
        while count <= noItems:
            print(f"\tEnter item #{count}: ")
            partNum = input("\t\tEnter part number: ")
            partDesc = input("\t\tEnter part description: ")
            partCost = float(input("\t\tEnter part cost: "))
            partQty = float(input("\t\tEnter quantity: "))
            itemSubtotal = partQty * partCost
            order.append(LineItem(partNum, partDesc, partCost, partQty, itemSubtotal))
            count += 1 
        return OrderInfo(orderNum, orderDesc, order)
    
    def calcOrderTotal(self):
        """Calculate invoice subtotal, tax, total"""
        invoiceSubTotal = 0.0
        i = 1
        for i in OrderInfo.lineItems:
            print("TBCompleted")
            invoiceSubTotal += lineItems.itemSubtotal[i]
        invoiceSubTotal = invoiceSubTotal
        invoiceTax = invoiceSubTotal * .075
        invoiceTotal = invoiceTax + invoiceSubTotal 
        return invoiceSubTotal, invoiceTax, invoiceTotal

    def getInvoice(self, customer, order):
        """Return order invoice string"""
        #self.calcOrderTotal()
        lineItemNums = len(order.lineItems)
        invoice = ""
        invoice += f"Customer : {customer.firstName}, {customer.lastName}, {customer.email}\n"
        for i in range(1, lineItemNums+1):
            invoice += f"\tLine #{i}"
 
        #invoice += f"\t\t\tTax: {self.invoiceSubTotal}\n"
        #invoice += f"\t\t\tTax: {self.invoiceTax}\n"
        #invoice += f"\t\tTotal Invoice: {self.invoiceTotal} lastName"

        #Start Here

        return invoice

if __name__ == '__main__':
    program = Program()
    program.main()