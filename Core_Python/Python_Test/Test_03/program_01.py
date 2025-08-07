# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             return False
#     return True

# def get_first_n_primes(n):
#     primes = []
#     num = 2
#     while len(primes) < n:
#         if is_prime(num):
#             primes.append(num)
#         num += 1
#     return primes

# n = int(input("Enter how many prime numbers you want: "))
# prime_list = get_first_n_primes(n)

# print("First", n, "prime numbers are:")
# for prime in prime_list:
#     print(prime, end=" ")


n = int(input("Enter n: "))
count = 0
num = 2
while count < n:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
        count += 1
    num += 1