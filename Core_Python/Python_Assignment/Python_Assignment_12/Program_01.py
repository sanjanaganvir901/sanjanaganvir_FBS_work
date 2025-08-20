s=input("Enter a string: ")
result=""
for ch in s:
    if ch=='a':
        result+='$'
    else:
        result+=ch
print("Result: ",result)