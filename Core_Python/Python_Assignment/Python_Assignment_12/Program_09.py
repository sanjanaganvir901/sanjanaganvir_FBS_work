s=input("Enter a string: ")
words=1
chars=0

for ch in s:
    chars+=1
    if ch==" ":
        words+=1

print("Words: ",words)
print("Characters: ",chars)