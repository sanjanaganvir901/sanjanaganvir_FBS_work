n = int(input("Enter number of employees: "))
total = 0
for i in range(n):
    basic = float(input(f"Enter basic salary of emp {i+1}: "))
    if basic < 20000:
        da = basic * 0.10
        ta = basic * 0.12
        hra = basic * 0.15
    else:
        da = basic * 0.15
        ta = basic * 0.18
        hra = basic * 0.20
    salary = basic + da + ta + hra
    total += salary
    print(f"Emp {i+1} total salary = {salary}")
print("Total salary of all employees =", total)
