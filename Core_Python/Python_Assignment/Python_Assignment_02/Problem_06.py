# WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.

basic = int(input("Enter a basic salary : "))

da = basic * (10/100)
ta = basic * (12/100)
haa = basic * (15/100)

total_salary = basic + da + ta + haa

print("Total salary of the employee is : ",total_salary)