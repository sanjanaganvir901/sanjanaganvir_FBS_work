side = int(input("Enter side of Wall : "))
cost_int = int(input("Enter cost of interior wall : "))
cost_ext = int(input("Enter Cost Of exterior wall : "))

total_area = 7 * side**2
total_cost = (total_area * cost_int) + (total_area * cost_ext)

print("Cost of Painting 2 rooms is : ₹",total_cost)