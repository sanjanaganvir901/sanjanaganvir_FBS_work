d={}
n=int(input("How many key-value pair?"))
for i in range(n):
    key=input("Enter key: ")
    value=int(input("Enter value: "))
    d[key]=value

product=1
for k in d:
    product*=d[k]

print("Product of values: ",product)