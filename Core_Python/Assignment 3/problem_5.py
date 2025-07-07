side1=int(input("enter the side1: "))
side2=int(input("Enter the side2: "))
side3=int(input("enter the side3: "))

if(side1==side2==side3):
    print("It is euilateral triangle")

elif(side1==side2 or side2==side3 or side3==side1):
    print("It is a isoscelous triangle")

else:
    print("It is a scalar triangle")