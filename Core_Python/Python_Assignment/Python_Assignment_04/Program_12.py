start=int(input("Enter start number: "))
stop=int(input("Enter stop number: "))

for i in range(start,stop+1):
    num=i
    count=0
    temp=num

    while(num!=0):
        num=num//10
        count+=1
    num=temp
    sum=0
    while(num!=0):
        a=num%10
        num=num//10
        sum=sum+(a**count)

    if(sum==temp):
        print("It is armstrong number",temp)
