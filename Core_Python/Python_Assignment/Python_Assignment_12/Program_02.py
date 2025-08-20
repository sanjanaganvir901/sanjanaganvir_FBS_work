s=input("Enter a string: ")
n=int(input("Enter index to remove:"))
result=""
for i in range(len(s)):
    if i!=n:
        result+=s[i]
print("Result: ",result)