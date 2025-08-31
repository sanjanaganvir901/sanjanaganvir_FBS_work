s=input("Enter a string: ")
no_vowels=''.join([ch for ch in s if ch.lower()not in "aeiou"])
print("String without vowels:",no_vowels)