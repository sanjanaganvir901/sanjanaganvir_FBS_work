# Program to calculate the percentage of student based on marks of any 5 subjects.
m1 = int(input("Enter a marks : "))
m2 = int(input("Enter a marks : "))
m3 = int(input("Enter a marks : "))
m4 = int(input("Enter a marks : "))
m5 = int(input("Enter a marks : "))

percentage = ((m1 + m2 + m3 + m4 + m5)/500)*100 #per=(total/500)*100
print("Percentage of Students : ",percentage)