n1=int(input("Size of first list: "))
a=[]
for i in range(n1):
    a.append(int(input()))

n2=int(input("Size of second list: "))
b=[]
for j in range(n2):
    b.append(int(input()))

m=a[:]
for x in b:m.append(x)

for i in range(len(m)-1):
    for j in range(len(m)-i-1):
        if m[j]>m[j+1]:
            m[j],m[j+1]=m[j+1],m[j]

print("Merged and Sorted: ",m)




