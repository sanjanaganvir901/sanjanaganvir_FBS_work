a1 = int(input("Enter age of person 1: "))
a2 = int(input("Enter age of person 2: "))
a3 = int(input("Enter age of person 3: "))
a4 = int(input("Enter age of person 4: "))
a5 = int(input("Enter age of person 5: "))

amt=int(input("Enter the amount: "))
total=0

if(a1<12):
    total+=amt-(amt*0.3)
elif(a1>59):
    total+=amt-(amt*0.5)
else:
   total+=amt

if(a2<12):
    total+=amt-(amt*0.3)
elif(a2>59):
    total+=amt-(amt*0.5)
else:
    total+=amt
    
if(a3<12):
    total+=amt-(amt*0.3)
elif(a3>59):
    total+=amt-(amt*0.5)
else:
    total+=amt
    
if(a4<12):
    total+=amt-(amt*0.3)
elif(a4>59):
    total+=amt-(amt*0.5)
else:
    total+=amt
    
if(a5<12):
    total+=amt-(amt*0.3)
elif(a5>59):
    total+=amt-(amt*0.5)
else:
    total+=amt

print("The total amount is: ",total)