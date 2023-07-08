def prime(n):
    i = 1
    while i != n :
        if n % i == 0 and i != n and i != 1:
            print("is not a prime number")
            return
        i += 1
    print("is a prime number")
print(prime(17))
        