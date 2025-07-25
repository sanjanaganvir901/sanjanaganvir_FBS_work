s1=int(input("Enter the marks os first subject: "))
s2=int(input("Enter the marks os second subject: "))
s3=int(input("Enter the marks os third subject: "))
s4=int(input("Enter the marks os fourth subject: "))
s5=int(input("Enter the marks os fifth subject: "))

total_marks=s1+s2+s3+s4+s5

per=0

per=total_marks/5

if(per>=80 and per<=100):
    print("Grade A")

elif(per>=70 and per<80):
    print("Grade B")

elif(per>=60 and per<70):
    print("Grade C")

elif(per>=40 and per<=60):
    print("Grade D")

elif(per<40 and per>=0):
    print("Fail")

else:
    print("Wrong Input")

print(total_marks/5)
