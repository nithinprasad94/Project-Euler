t0 = 0
t1 = 1
t2 = 0
sum = 0

while t1 < 4000000:
    t2 = t1 + t0

    if t2%2 == 0:
        sum += t2

    t0 = t1
    t1 = t2

print sum
    
