import random

userid=input("Enter the userid: ")
pass1=input("Enter the password: ")

if(userid=="siya" and pass1=='siya123'):
    captcha=random.randint(1000,9999)
    print(captcha)
    user_captcha=input("Enter the captcha: ")
    print("Sucessfully login")

else:
    print("Fail")
