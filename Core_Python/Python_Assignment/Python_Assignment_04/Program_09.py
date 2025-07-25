start=int(input("Enter the start number: "))
stop=int(input("Enter stop number: "))
div=int(input("Enter which number do you want to divide: "))

num=0
for i in range(start,stop):
    if(i%div==0):
        print(i)
    
        