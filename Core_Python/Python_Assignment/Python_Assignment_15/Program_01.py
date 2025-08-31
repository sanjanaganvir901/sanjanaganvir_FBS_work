class Book:
    def __init__(self,b_id=0,b_name="",price=0,author=""):
        self.b_id=b_id
        self.b_name=b_name
        self.price=price
        self.author=author

    def __del__(self):
        print("Deleting Book:",self.b_name)

    def ShowBook(self):
        print("b_id:",self.b_id)
        print("b_name: ",self.b_name)
        print("price:",self.price)
        print("author:",self.author)

print("Without parameters constructor")
obj1=Book()
obj1.ShowBook()

print("With parameters contructor")
obj2=Book(101,"Python",550,"Guido van rossum")
obj2.ShowBook()