side1=int(input("enter the side1: "))
side2=int(input("Enter the side2: "))
side3=int(input("enter the side3: "))

if(side1+side2>side3 and side2+side3>side1 and side3+side1>side2):
    print("Tiangle is valid")

else("Triangle is not valid")