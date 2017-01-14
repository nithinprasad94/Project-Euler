import math

#Factorize an input number, and return the factor list
def factorize(num):

    factor_list = []

    for i in range(1,int(math.floor(num**0.5))+1):

        if num%i == 0:
            factor_1 = i
            factor_2 = num/i

            factor_list.append(factor_1)

            if (factor_1 != factor_2):
                factor_list.append(factor_2)

    factor_list.sort()

    return factor_list

#Find a factor list of size 500 for Triangle Numbers
i = 1
add_next = 2
factor_list = []
found_num = 0

while len(factor_list) <= 500:

    factor_list = factorize(i)

    if (len(factor_list) > 500):
        found_num = i        

    i += add_next
    add_next += 1

print found_num
        

    
    
