s = input("Enter a string: ")
words = []
counts = []

word = ""
for ch in s + " ":
    if ch != " ":
        word += ch
    else:
        if word != "":
            found = False
            for i in range(len(words)):
                if words[i] == word:
                    counts[i] += 1
                    found = True
            if not found:
                words.append(word)
                counts.append(1)
            word = ""

for i in range(len(words)):
    print(words[i], ":", counts[i])