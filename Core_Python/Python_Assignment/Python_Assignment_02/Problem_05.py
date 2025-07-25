# WAP to calculate selling price of book based on cost price and discount.

cost_price = int(input("Enter a cost price of book : "))
marked_price = int(input("Enter a marked price of book : "))
discount_percent = int(input("Enter a discount percentage : "))

discount_amount = (discount_percent / 100)*marked_price
selling_price = marked_price - discount_amount

print("Selling price of the book is : ",selling_price)