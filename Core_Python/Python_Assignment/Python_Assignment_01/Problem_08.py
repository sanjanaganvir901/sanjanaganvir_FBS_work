# A program to convert days into years, weeks and days.

days = int(input("Enter number of days : "))

years = days // 365#2
days =  days % 365
weeks = days // 7
days = days % 7
print("Years : ",years,"Weeks : ",weeks,"Days : ",days)