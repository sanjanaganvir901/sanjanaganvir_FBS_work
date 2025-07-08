length = int(input("Enter length of the room: "))
width=int(input("Enter width of the room: "))
height = int(input("Enter height of the room: "))
cost = int(input("Enter the cost : "))

area = 2 * (length + width ) * height
total_cost = area * cost

print("Total cost of painting :", total_cost)
