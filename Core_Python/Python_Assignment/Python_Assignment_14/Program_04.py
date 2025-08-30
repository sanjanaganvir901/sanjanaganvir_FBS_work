n=int(input("Enter the size: "))
a=[int(input())for i in range(n)]
target=int(input("Enter target: "))

for i in range(n):
    for j in range(i+1,n):
        if a[i]+a[j]==target:
            print(a[i],a[j])