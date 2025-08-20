d={}
n=int(input("How many key-value pair?"))
for i in range(n):
    key=input("Enter key: ")
    value=int(input("Enter value:"))
    d[key]=value

total=0
for k in d:
    total+=d[k]

print("Sum of values: ",total)