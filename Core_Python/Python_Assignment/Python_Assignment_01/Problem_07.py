#Find teh roots of a Quadratic Equation

a = float(input("Enter a number : "))
b = float(input("Enter a number : "))
c = float(input("Enter a number : "))

x1 = (-b + (b**2 - 4 * a * c)**0.5) / 2 * a
x2 = (-b - (b**2 - 4 * a * c)**0.5) / 2 * a

print("The Quadratic Equation is : ",x1,x2)