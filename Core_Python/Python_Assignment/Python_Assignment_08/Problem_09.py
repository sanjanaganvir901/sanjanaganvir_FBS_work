def Palindrome(num,rev):
    if(num!=0):
        a = num % 10
        rev = rev * 10 + a
        return Palindrome(num // 10,rev)
    else:
        return rev
num = int(input("Enter a number : "))
ans = Palindrome(num,0)
if(ans==num):
    print("The number is Palindrome")
else:
    print("The number is Not palindrome")