s=input("Enter a string: ")
letters=0
digits=0

for ch in s:
    if '0'<=ch<='9':
        digits+=1

    elif('a'<=ch<='z') or ('A'<=ch<='Z'):
        letters+=1

print("Letters: ",letters)
print("Digits: ",digits)