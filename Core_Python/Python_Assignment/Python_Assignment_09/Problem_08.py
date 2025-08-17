def prime(n,i=2):
    if n <= 1:
        return False
    if n == 2:
        return True 
    if n % i == 0:
        return False
    if i * i > n:
        return True 
    return prime(n,i+1)

n=int(input("Enter the number: "))

if prime(n):
    print("It is a prime number")

else:
    print("It number is not prime number")

