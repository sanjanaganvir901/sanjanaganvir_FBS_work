s=input("Enter a String: ") 
word="" 
words=[]
freq={}

for ch in s + " ":
    if ch!=" ":
        word+=ch

    else:
        if word!="":
            words.append(word)
            word=""

for w in words:
    if w in freq:
        freq[w]=freq[w]+1
    else:
        freq[w]=1
for k in freq:
    print(k,":",freq[k])
            