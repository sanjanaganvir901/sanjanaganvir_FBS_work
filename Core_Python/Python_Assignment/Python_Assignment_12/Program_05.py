s=input("Enter a string: ")
vowels="aeiouAEIOU"
count=0
for ch in s:
    for v in vowels:
        if ch==v:
            count+=1

print("Vowels:",count)