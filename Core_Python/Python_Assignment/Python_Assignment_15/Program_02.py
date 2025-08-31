class Product:
    def __init__(self,p_id=0,p_name="",price=0,quantity=0):
        self.p_id=p_id
        self.p_name=p_name
        self.price=price
        self.quantity=quantity

    def __del__(self):
        print("Deleting Product:",self.p_name)

    def ShowBook(self):
        print("p_id:",self.p_id)
        print("p_name: ",self.p_name)
        print("price:",self.price)
        print("quantity:",self.quantity)

print("Without parameters constructor")
obj1=Product()
obj1.ShowBook()

print("With parameters contructor")
obj2=Product(2046,"cleanser",550,10)
obj2.ShowBook()