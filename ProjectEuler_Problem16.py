#Digit Mapper Function
def digit_mapper(digit,carry):

    if digit <= 4:
        return (0,2*digit+carry)
    else:
        if digit == 5:
            return (1,0+carry)
        elif digit == 6:
            return (1,2+carry)
        elif digit == 7:
            return (1,4+carry)
        elif digit == 8:
            return (1,6+carry)
        elif digit == 9:
            return (1,8+carry)

def number_processor(num):

    num_str = str(num)
    dig_list = [int(dig) for dig in num_str]
    print dig_list

    new_list = [0]*(len(dig_list) + 1) #In case carry overflows
    #print new_list
    new_digit = 0
    carry = 0
    #print len(dig_list)-1
    for digit in range(len(dig_list)-1,-1,-1):
        (carry,new_digit) = digit_mapper(dig_list[digit],carry)
        new_list[digit+1] = new_digit

    new_list[0] = carry

    if carry == 0:
        new_list = new_list[1:]

    ret_list = []
    
    for elem in new_list:
        ret_list.append(str(elem))
    
    return ret_list

#Run functionality
base = 1

for i in range(1000):

    new_list = number_processor(base)
    num = ''.join(new_list)
    base = int(num)

print base
base_str = str(base)
base_list = [int(char) for char in base_str]
sum_digits = sum(base_list)
print sum_digits
    
        

###Brute force alg
##for i in range(701):
##    num = 2**i
##    num_str = str(num)
##    num_digits = [int(dig) for dig in num_str]
##    sum_digits = sum(num_digits)
##    print "2**" + str(i) + ": " + str(num) + ", " + str(sum_digits)

