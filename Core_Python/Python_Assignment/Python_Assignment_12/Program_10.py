s1=input("Enter first string: ")
s2=input("Enter second string: ")
len1,len2=0,0
for ch in s1:
    len1+=1
for ch in s2:
    len2+=1

if len1>len2:
    print("Larger String:",s1)

elif len2>len1:
    print("Larger String:",s2)

else:
    print("Both are equal")