for i in range(0,4):
    for j in range(4-i-1):
        print(" ",end=" ")
    k=1
    for j in range(i+1):
        print(k,end='   ')
        k = k * (i-j)//(j+1)
    print()