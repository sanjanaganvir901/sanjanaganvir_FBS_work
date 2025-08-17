n=int(input("Enter number of elements: "))
list1=[]

for i in range(n):
    val=int(input(f"Enter elements{i+1}:"))
    list1.append(val)

even_list=[]
odd_list=[]

for num in list1:
    if num%2==0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Original list: ",list1)
print("Even list: ",even_list)
print("Odd list: ",odd_list)

