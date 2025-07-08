p1=int(input("Enter the price of first product: "))
p2=int(input("Enter the price of second product: "))
p3=int(input("Enter the price of third product: "))
p4=int(input("Enter the price of fourth product:"))
p5=int(input("Enter the price of fifth product: "))

total_bill=p1+p2+p3+p4+p5

print("The total bill is: ",total_bill)
gst = total_bill * 0.18

total_bill = total_bill + gst
print("Total bill after GST: ", total_bill)
