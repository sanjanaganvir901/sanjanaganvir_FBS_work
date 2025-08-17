n=int(input("Enter number of elements:"))
list1=[]

for i in range(n):
    num=int(input(f"Enter list1{i+1}:"))
    list1+=[num]

cubes=[0]*n
for i in range(n):
    cubes[i]=list1[i]*list1[i]*list1[i]

print("Original List:",list1)
print("Cube List:",cubes)