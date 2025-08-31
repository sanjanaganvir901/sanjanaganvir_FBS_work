s=input("Enter a string:")
short_words=[word for word in s.split() if len(word)<5]
print("Words with less than 5 letters",short_words)