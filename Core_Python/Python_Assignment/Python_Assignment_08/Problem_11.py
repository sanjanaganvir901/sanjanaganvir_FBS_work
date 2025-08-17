def count(num):
    if num!=0:
        return 1+count(num//10)
    else:
        return 0
    
def armstrong(num,digits):
    temp=num
    sum=0
    while temp>0:
        digit=temp%10
        sum+=digit ** digits
        temp=temp//10
    return sum

num=int(input("Enter a number: "))
c=count(num)
ans=armstrong(num,c)

if ans==num:
    print("Yes,it is a armstrong number")
else:
    print("No,it is not a armstrong number")