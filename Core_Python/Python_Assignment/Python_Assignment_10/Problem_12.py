n=int(input("Enter how many numbers:"))

numbers=[0]*n
squares=[0]*n
cubes=[0]*n
for i in range(n):
    num=int(input(f"Enter number{i+1}:"))
    numbers[i]=num
    squares[i]=num*num
    cubes[i]=num*num*num


print("Numbers: ",numbers)
print("Squares: ",squares)
print("Cubes: ",cubes)