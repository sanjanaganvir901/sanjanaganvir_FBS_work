p1 = int(input("Enter a product 1 : "))
p2 = int(input("Enter a product 2 : "))
p3 = int(input("Enter a product 3 : "))
p4 = int(input("Enter a product 4 : "))
p5 = int(input("Enter a product 5 : "))

total_bill = p1+p2+p3+p4+p5

total = total_bill+(total_bill*0.18)
print("Total bill after adding 18% GST : ",total)