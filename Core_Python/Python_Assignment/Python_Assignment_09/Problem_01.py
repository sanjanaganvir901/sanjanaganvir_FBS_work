def fact(n):
    if (n==0 or n==1):
        return 1
    return n*fact(n-1)

def sumofseries(n):
    if(n==0):
        return 0
    return fact(n)+sumofseries(n-1)

n=int(input("Enter the number: "))
print("Sum of the series is:",sumofseries(n))