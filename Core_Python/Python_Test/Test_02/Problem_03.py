length = 50
breadth = 40
radius = 20
round = 5
cost_per_meter = 35

rectangle = length + 2 * breadth
semicircle = 3.14 * radius

total_perimeter = rectangle + semicircle

total_wire = total_perimeter * round
total_cost = total_wire * cost_per_meter

print("The total cost of fencing the field is : ",total_cost)