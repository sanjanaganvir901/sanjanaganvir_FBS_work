def memoize(func):
    cache={}
    def wrapper(n):
        if n in cache:
            print("Fetching from cache for",n)
            return cache[n]
        else:
            print("Computing new result for",n)
            result=func(n)
            cache[n]=result
            return result
    return wrapper

@memoize
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

print(factorial(5))