class Customer:
    customer_name = []

    def __init__(self, name ):
        self.name = name
        Customer.customer_name.append(self)
           

    @property
    def name(self):
        return self._name #getter method
    
    @name.setter
    def name(self,value):
        if isinstance(value , str ) and len(1 <= value <= 15):
            self._name = value # store this in the internal variable 
        else:
            raise ValueError("Name shoule between 1-15 characters long")    
    def orders(self):
        # i want to return a list of the oders for this particular custommer
        from order import Order
        return [order for order in Order.all if order.customer == self]    
    def coffee(self):
        #should returns a list of all coffee linked to the customer
        return list({order.coffee for order in self.Orders()})
    
    def total_spent(self):
        return sum(order.price for order in self.orders())