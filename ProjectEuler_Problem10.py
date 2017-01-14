#Function to see if any factors divide into number
def isDiv(factors,x):
    for factor in factors:
        if x%factor == 0:
            return True
        else:
            pass
    return False

#Accumulate primes until counter hits 2 million, then sum them
primes = [2]
counter = 2

while counter <= 2000000:
    if isDiv(primes,counter):
        pass
    else:
        primes.append(counter)
    counter += 1
    if counter%10000 == 0:
        print counter

print counter
print sum(primes)
