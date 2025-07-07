sp=int(input("Enter the selling price: "))
cp=int(input("enter the cost price: "))

if sp > cp:
    p = sp - cp
    print("You are in a profit ")

elif sp < cp:
    l = cp - sp
    print("You are in a loss ")

else:
    print("No profit, no loss.")
