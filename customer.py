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
        
