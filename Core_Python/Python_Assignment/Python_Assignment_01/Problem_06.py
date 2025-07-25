# A program to input two angle from user and find third angle of the triangle
angle1 = float(input("Enter a first angle : "))
angle2 = float(input("Enter a second angle : "))

angle3 = 180 - (angle1 + angle2)
# angle = 180 - (40+60)=80
print("The Third angle is : ",angle3)