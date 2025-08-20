d={}
n=int(input("How many key-value pair?"))
for i in range(n):
    key=input("Enter key: ")
    value=int(input("Enter value: "))
    d[key]=value

search_key=input("Enter key to search:")
found=False
for k in d:
    if k==search_key:
        found=True
        break

if found:
    print("Key exist")

else:
    print("Key not found")