d1={}
d2={}

n1=int(input("How many pairs in first dict?"))
for i in range(n1):
    key=input("Enter key:")
    value=int(input("Enter value: "))
    d1[key]=value

n2=int(input("How many pairs in second dict?"))
for i in range(n2):
    key=input("Enter key:")
    value=int(input("Enter value: "))
    d2[key]=value

for k in d2:
    d1[k]=d2[k]

print("Concatenated Dictonary: ",d1)