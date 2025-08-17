n1=int(input())
a=[int(input())for i in range(n1)]
n2=int(input())
b=[int(input())for i in range(n2)]

u=a[:]
for x in b:
    f=0
    for y in u:
        if x==y:
            f=1
            break

    if not f:u.append(x)

print(u)
