###Function to determine if a number is divisible by all numbers in a range, evenly
def isDivEven(factor_list,x):
    for i in factor_list:
        if x%i == 0:
            pass           
        else:
            return False
    return True

##def fact(x):
##    if x == 0 or x == 1:
##        return x
##    else:
##        return x*fact(x-1)

prod = 1
for i in range(1,21):
    print "i: ",i
    #If current product is divisible by i and preceding i's, do nothing
    if isDivEven(range(1,i+1),prod):
        pass

    #Otherwise, multiply prod by increasing factors until prod is div by i
    else:
        base = 2
        while not(isDivEven(range(1,i+1),prod)):
            if isDivEven(range(1,i+1),base*prod):
                prod = base*prod
            else:
                base = base+1

print prod

for i in range(1,21):
    if isDivEven(range(1,21),prod/i):
        print prod/i
        print "yeehaw"
        

