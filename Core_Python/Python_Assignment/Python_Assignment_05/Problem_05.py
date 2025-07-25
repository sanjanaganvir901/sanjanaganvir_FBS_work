for i in range(1,6):
    for j in range(1,7-i):
        print(" ",end=' ')

    for j in range(1,i+1):
        print("*",end=" ")
    j=j+1
    for j in range(1,i):
        print("*",end=" ")
        j+=1
    print()