n=int(input("Enter size: "))
a=[int(input())for i in range(n)]

max1=-99999
max2=-99999

for x in a:
    if x>max1:
        max2=max1
        max1=x
    elif x>max2:
        max2=x

print(max1,max2,max1*max2)

