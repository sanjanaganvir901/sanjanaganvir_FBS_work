p = int(input("Enter a Principle : "))
t = int(input("Enter a Time : "))
r = int(input("Enter a Rate : "))
CI = p * (1 + r/100) ** t - p
print("Compound Interest is : ",CI)
