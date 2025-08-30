n=int(input("Enter number of words:"))
words=[input()for i in range(n)]
used=[0]*n

for i in range(n):
    if used[i]==0:
        group=[words[i]]
        used[i]=1

        for j in range(i+1,n):
            if used[j]==0:
                if sorted(words[i])==sorted(words[j]):
                    group.append(words[j])
                    used[j]=1
        print(group)