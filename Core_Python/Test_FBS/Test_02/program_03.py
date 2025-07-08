radius=20
length=50
breadth=40
cost=35

rectangle=2*(length+breadth)
half_circle=3.14*radius
total_one_round=rectangle+half_circle
total_fence=total_one_round*5

total_cost=total_fence*cost

print("total cost of fencing is",total_cost)