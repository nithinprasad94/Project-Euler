import math

#Brute Force
quest = 600851475143
factors = []

#Function to see if number is prime
def isPrime(x):

    primes = [2]
    
    for i in range(2,int(math.ceil(x**0.5))):
        if x%i == 0:
            return False
        else:
            pass
        
    return True

#1) Find all factors of quest
for i in range(2,int(math.ceil(quest**0.5))):
    if quest%i == 0:
        factors.append(i)
print factors

#2) Reduce set of factors to set of prime factors    
prime_factors = []

for i in factors:
    if isPrime(i):
        prime_factors.append(i)

#3) Print max prime factor
print max(prime_factors)
