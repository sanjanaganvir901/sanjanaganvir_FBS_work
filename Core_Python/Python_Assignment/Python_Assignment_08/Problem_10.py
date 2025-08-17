def CheckLeap(years):
    if(years%400==0) or (years%4==0 and years%100!=0):
        return True
    else:
        return False


years = int(input("Enter the year : "))
if CheckLeap(years):
    ("The year is Leap")
else:
    print("The year is Not Leap")