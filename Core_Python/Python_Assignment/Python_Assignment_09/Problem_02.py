def power_sum(num,power):
    if (num==0):
        return 0
    return (num%10)**power + power_sum(num//10,power)

def armstrong(num):
    digits=len(str(num))
    return num==power_sum(num,digits)

n=int(input("Enter the number: "))

if armstrong(n):
    print("The number is Armstrong")

else:
    print("The number is not Armstrong")