class Order:
    all= []

    def __init__(self,customer,coffee,price):
        #customer validation 
        from customer import Customer
        if not isinstance(customer, Customer):
            raise TypeError("Customer not in data base ")
        
        #validate coffee
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee not in data base ")
        # validate the price 
        if not isinstance(price, float ):
            raise TypeError("Price must be a float")
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be btw 1.0 and 10.0")
        
        self._customer = customer
        self._coffee = coffee
        self._price = price 

        Order.all.append(self)

    @property
    def customer(self):
        return self._customer
    @property
    def coffee(self):
        return self._coffee
    @property
    def price(self):
        return self._price
             