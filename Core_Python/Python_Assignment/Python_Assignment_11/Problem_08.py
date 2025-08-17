n = 10  
num = 100
for row in range(10):
    row_numbers = []
    for col in range(n):
        row_numbers.append(num)
        num -= 1
    if row % 2 == 1:  
        for i in range(len(row_numbers)//2):
            temp = row_numbers[i]
            row_numbers[i] = row_numbers[len(row_numbers)-1-i]
            row_numbers[len(row_numbers)-1-i] = temp
    for val in row_numbers:
        print(val, end="\t")
    print()