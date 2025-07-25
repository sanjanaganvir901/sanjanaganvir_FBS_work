# Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount

amount = int(input("Enter a amount :"))

n500 = amount // 500
r_amount = amount % 500

n200 = r_amount // 200
r_amount = r_amount % 200

n100 = r_amount // 100
r_amount =  r_amount % 100

n50 = r_amount // 50
r_amount = r_amount % 50

n20 = r_amount // 20
r_amount = r_amount % 20

n10 = r_amount // 10
r_amount = r_amount % 10

print("Total amount is enter by the user is : ",amount)
print("Note of $500 :",n500)
print("Note of $200",n200)
print("Note of $100",n100)
print("Note of $50",n50)
print("Note of $20",n20)
print("Note of $10",n10)