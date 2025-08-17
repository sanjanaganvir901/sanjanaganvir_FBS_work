def reverse(num,rev=0):
    if(num!=0):
        a=num%10
        rev=rev*10+a
        return reverse(num//10,rev)
    else:
        return rev

num=int(input("Enter the number: "))
ans=reverse(num)
print("The reverse number is",ans)
