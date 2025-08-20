d={}
n=int(input("How many key-value pair?"))
for i in range(n):
    key=input("Enter key: ")
    value=int(input("Enter value: "))
    d[key]=value

remove_key=input("Enter key to  remove: ")

new_dict={}
for k in d:
    if k!=remove_key:
        new_dict[k]=d[k]

print("Dictionary after removal: ",new_dict)