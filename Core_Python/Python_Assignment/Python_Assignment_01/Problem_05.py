# A program to enter p,t,r and calculate Compound Interest

p = int(input("Enter a Principle : "))
t = int(input("Enter a Time : "))
r = int(input("Enter a Rate : "))

CI = p * (1 + r/100) ** t - p
print(f"Compound Interest is : {CI}")