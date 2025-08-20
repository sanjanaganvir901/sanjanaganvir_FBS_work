d={}
n=int(input("How many key-value pairs?"))

for i in range(n):
    key=input("Enter key: ")
    value=int(input("Enter value: "))
    d[key]=value
print("Dictionary: ",d)