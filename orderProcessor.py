from orderClasses import Customer, OrderInfo, LineItem

class Program:
    def main(self):
        """ Application starting point """
        print("Order processing application")
        customer = self.getCustomerInfo()
        orderLines = self.getOrderLines()
        OrderInfo.order = orderLines
        # Output invoice
        invoice = OrderInfo.getInvoice()
        print("\nCustomer Invoice\n")
        print(invoice)

    def getCustomerInfo(self):
        print("Enter customer information: ")
        firstName = input("\tEnter first name: ")
        lastName = input("\tEnter last name: ")
        email = input("\tEnter email address: ")
        return Customer(firstName, lastName, email)
    
    def getOrderLines(self):
        print("\nCreate order:")
        orderLines = []
        orderNum = input("\tEnter order number: ")
        orderDesc = input("\tEnter order description: ")
        noItems = int(input("\tHow many items are you ordering? "))
        count = 1
        print("\nEnter order details")
        while count <= noItems:
            print(f"Enter item #{count}: ")
            partNum = input("\tEnter part number: ")
            partDesc = input("\tEnter part description: ")
            partCost = float(input("\tEnter part cost: "))
            partQty = float(input("\tEnter quantity: "))
            itemSubtotal = partQty * partCost
            orderLines.append(LineItem(partNum, partDesc, partCost, partQty, itemSubtotal))
            count += 1 
        return orderLines
        
if __name__ == '__main__':
    program = Program()
    program.main()