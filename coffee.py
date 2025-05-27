class Coffee:
    shake =[]
    def __init__(self,name):
        if isinstance(name,str ) and len({name} >= 3):

         self._name = name
        else:
           raise ValueError("Name must be atleat 3 cjaracters long ")
        Coffee.shakey.append(self)

    @property
    def name(self):
       return self._name  # getter def method   

    def orders(self):
       from order import Order
       return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
       return list({order.customer for order in self.orders()})