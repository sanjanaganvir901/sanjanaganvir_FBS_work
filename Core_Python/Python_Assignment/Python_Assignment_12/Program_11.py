s=input("Enter a string: ")
result=""
for ch in s:
    if ch==" ":
        result+="_"
    else:
        result+=ch
print("Result: ",result)