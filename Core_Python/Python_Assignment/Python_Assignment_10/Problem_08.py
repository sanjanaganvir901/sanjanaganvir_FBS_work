n=int(input("enter the number of elements: "))
original_list=[]

for i in range(n):
    num=int(input(f"Enter number{i+1}:"))
    original_list.append(num)

duplicate_list=original_list[:]

print("Original List:",original_list)
print("Duplicate List:",duplicate_list)

print("Are they pointing to the same list?",original_list is duplicate_list)



