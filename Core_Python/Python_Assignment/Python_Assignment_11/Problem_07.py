n1 = int(input())
a = [int(input()) for i in range(n1)]
n2 = int(input())
b = [int(input()) for i in range(n2)]

for x in a:
    for y in b:
        if x == y:
            print(x, end=" ")
            break