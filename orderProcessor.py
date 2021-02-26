from orderClasses import Customer, OrderInfo, LineItem

class Program:
    def main(self):
        """ Application starting point """
        print("Order processing application")
        customer = self.getCustomerInfo()
        order = self.getOrder()
        # Output invoice
        invoice = self.getInvoice(customer, order)
        print("\nCustomer Invoice for ")
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
    
    def getInvoice(self, customer, order):
        """Return order invoice string"""
        lineItemNums = len(order.lineItems)
        invoice = ""
        invoice += f"Customer : {customer.firstName} {customer.lastName} \tEmail: {customer.email}\n"
        invoice += f"Order number: {order.lineItems[0].orderNum} Order description: {order.lineItems[0].orderDesc}\n"
        invoice += f"\t\tPart\tDescription\tCost\tQty\n"
        invoiceSubTotal = 0.0
        for i in range(1, lineItemNums):
            invoice += f"\tLine #{i}\t{order.lineItems[i].partNum}\t{order.lineItems[i].partDesc}\t{order.lineItems[i].partCost}\t{order.lineItems[i].partQty}\t{order.lineItems[i].itemSubtotal:.2f} \n"
            invoiceSubTotal += order.lineItems[i].itemSubtotal
        invoice += f"\t\t\t\t\t     Sub total: {invoiceSubTotal:,.2f}\n"
        invoiceTax = invoiceSubTotal * 0.075
        invoice += f"\t\t\t\t\t\t    Tax: {invoiceTax:,.2f}\n"
        invoiceTotal = invoiceSubTotal + invoiceTax
        invoice += f"\t\t\t\t\t   Order Total: {invoiceTotal:,.2f}\n"
        return invoice

if __name__ == '__main__':
    program = Program()
    program.main()