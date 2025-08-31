class Shirt:
    def __init__(self,s_id=0,s_name="",type="",price=0,size=""):
        self.s_id=s_id
        self.s_name=s_name
        self.type=type
        self.price=price
        self.size=size

    def __del__(self):
        print("Deleting Shirt:",self.s_name)

    def ShowBook(self):
        print("s_id:",self.s_id)
        print("s_name: ",self.s_name)
        print("type: ",self.type)
        print("price:",self.price)
        print("size:",self.size)

print("Without parameters constructor")
obj1=Shirt()
obj1.ShowBook()

print("With parameters contructor")
obj2=Shirt(1211,"Cotton Shirt","Formal",550,"Small")
obj2.ShowBook()