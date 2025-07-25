length = int(input("Enter a length : "))
breadth = int(input("Enter a breadth : "))
height = int(input("Enter a height : "))
cost_per_meter = int(input("Enter a cost per meter :"))

perimeter = 2*height * (length+breadth)
total_wall = 4 * perimeter
total_cost_painting = total_wall * cost_per_meter
print("The total cost of penting is : ",total_cost_painting)