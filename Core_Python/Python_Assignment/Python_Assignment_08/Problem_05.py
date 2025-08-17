def PrimeNo(n):
    total = 0
    for num in range(2,n+1):
        count = 0
        for i in range(1,num+1):
            if(num%i==0):
                count+=1
        if count == 2:
            total+=num
            print(num)
    return total
n = int(input("Enter a number : "))
print(f"Sum of Prime Number from 1 to : {n} is {PrimeNo(n)}")