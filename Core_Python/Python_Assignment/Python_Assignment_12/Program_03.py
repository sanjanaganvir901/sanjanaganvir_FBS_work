s1=input("Enter first string: ")
s2=input("Enter second string: ")

if len(s1)!=len(s2):
    print("Not Anagram")

else:
    s1_count=[0]*256
    s2_count=[0]*256

    for i in range(len(s1)):
        s1_count[ord(s1[i])]+=1
        s2_count[ord(s2[i])]+=1

    if s1_count==s2_count:
        print("It is a Anagram string")

    else:
        print("It is not a Anagram string")

