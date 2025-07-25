num = int(input("Enter a number : "))

last = num % 10
num = num // 10
middle = num % 10
first = num // 10

if(first == 2 * middle and first * 2 == last):
    print("yes")
else:
    print("No")

# first = num // 100
# second = (num // 10) % 10
# third = num % 10