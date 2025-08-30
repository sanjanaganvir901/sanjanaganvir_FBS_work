n=int(input("Enter size: "))
a=[int(input())for i in range(n)]
target=int(input("Enter target: "))

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if a[i]+a[j]+a[k]==target:
                print(a[i],a[j],a[k])