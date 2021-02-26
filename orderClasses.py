class Customer:
    def __init__(self, firstName, lastName, email):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email

class OrderInfo:
    def __init__(self, orderNum, orderDesc, lineItems = None):
        self.orderNum = orderNum
        self.orderDesc = orderDesc
        self.lineItems = lineItems or []

class LineItem:
    def __init__(self, partNum, partDesc, partCost, partQty, itemSubtotal):
        """Order line items"""
        self.partNum = partNum
        self.partDesc = partDesc
        self.partCost = partCost
        self.partQty = partQty
        self.itemSubtotal = itemSubtotal
