n=int(input("Enter a number of elements: "))
list1=[]

for i in range(n):
    num=int(input(f" Enter number{i+1}:"))
    list1.append(num)

i=0
while i < len(list1):
    j=i+1
    while j<len(list1):
        if(list1[i]==list1[j]):
            k=j
            while k<len(list1)-1:
                list1[k]=list1[k+1]
                k+=1
            list1=list1[:-1]
        else:
            j+=1
    i+=1
print("After remove duplicates from the list",list1) 