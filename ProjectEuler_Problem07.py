#Function to see if any factors divide into number
def isDiv(factors,x):
    for factor in factors:
        if x%factor == 0:
            return True
        else:
            pass
    return False

#Count until 10001th prime number is reached
primes = [2]
num_primes = len(primes)
i = 2 #Start the counter at 2

while num_primes < 10001:
    if isDiv(primes,i):
        pass
    else:
        primes.append(i)
        num_primes = len(primes)
    i += 1

print i
print primes[-1]
