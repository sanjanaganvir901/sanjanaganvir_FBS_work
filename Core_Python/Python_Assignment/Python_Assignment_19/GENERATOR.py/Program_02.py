def palindrome_gen():
    num=1
    while True:
        if str(num)==str(num)[::-1]:
            yield num
        num+=1

pal_gen=palindrome_gen()
for i in range(10):
    print(next(pal_gen),end=" ")