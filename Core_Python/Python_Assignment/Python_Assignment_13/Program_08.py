s=input("Enter a string: ")
words=[]
word=""

for ch in s+" ":
    if ch!=" ":
        word+=ch
    else:
        if word!="":
            words.append(word)
            word=""

freq={}
for w in words:
    if w in freq:
        freq[w]+=1
    else:
        freq[w]=1

print("Words Frequency: ",freq)