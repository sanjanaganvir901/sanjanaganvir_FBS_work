n1=int(input("Enter size of first list: "))
a=[int(input())for i in range(n1)]

n2=int(input("Enter size of second list: "))
b=[int(input())for i in range(n2)]

print("Misiing in B: ",end=" ")
for x in a:
    f=0
    for y in b:
        if x==y:
            f=1
    if f==0:
        print(x,end=" ")

print("\nMissing in A: ",end=" ")
for y in b:
    f=0
    for x in a:
        if y==x:
            f=1
    if f==0:
        print(y,end=" ")