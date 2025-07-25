# A program to enter p,t,r and calculate simple interest

p = int(input("Enter a principle : "))
t = int(input("Enter a Time : "))
r = int(input("Enter a Rate : "))

interest = (p * t * r)/100
# Principle, Time, Rate
print("Simple interest is : ",interest)