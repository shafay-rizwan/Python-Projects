nums =  range(1,50)
def my_prime(num):
    for x in range(2,num):
        if(num % x) == 0:
            return False
    return True

primes = list(filter(my_prime, nums ))

print(primes)

