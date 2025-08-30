n=int(input("Enter number of words: "))
words=[input()for i in range(n)]
prefix=""

for i in range(len(words[0])):
    ch=words[0][i]
    f=0
    for j in range(1,n):
        if i>=len(words[j]) or words[j][i]!=ch:
            f=1
    if f==0:
        prefix+=ch
    else:
        break
print(prefix)