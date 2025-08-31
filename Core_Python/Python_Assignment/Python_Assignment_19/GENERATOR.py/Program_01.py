def fibbo_gen(limit):
    a=0
    b=1
    while a<=limit:
        yield a
        a,b=b,a+b

limit=int(input("Enter limit for fibbonacci: "))
for num in fibbo_gen(limit):
    print(num,end=" ")