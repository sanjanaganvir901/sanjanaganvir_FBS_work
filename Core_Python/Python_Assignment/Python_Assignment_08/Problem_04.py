def sum_of_odd(n):
    total=0
    for i in range(1,n+1):
        if(i%2!=0):
            print(i)
            total+=i
    return total
        
n=int(input("Enter the value : "))
result=sum_of_odd(n)
print("sum of all odd numbers from 1 to",n,"is:",result)
