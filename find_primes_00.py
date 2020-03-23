#Finding Primes
def Sieve(n):
    numbers = list(range(2,n+1))
    primes = []
    for p in range(len(numbers)):
        if numbers[p] != 0:
            primes.append(numbers[p])
            for i in range(numbers[p], n + 1, numbers[p]):
                numbers[i - 2] = 0
    return primes
primes100 = Sieve(100)
print(primes100)