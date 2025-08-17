n = int(input("Enter number of elements: "))
a = list()
for i in range(n):
    a.append(int(input()))

size = len(a)
i = 0
while i < size:
    if a[i] % 2 == 0:   
        for j in range(i, size-1):
            a[j] = a[j+1]   
        size -= 1           
    else:
        i += 1

for k in range(size):
    print(a[k], end=" ")