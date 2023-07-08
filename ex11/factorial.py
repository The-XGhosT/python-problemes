def factorial(n):
    i = 0
    res = 1
    while(n - i) :
        res *= n - i
        i += 1
    return res
print(factorial(4))