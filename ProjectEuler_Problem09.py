import math

#Define a function that checks if the sum of 2 squares has an integer root
def has_int_root(a,b):

    c_square = a**2 + b**2
    c = c_square**0.5
    c_ceil = math.ceil(c)
    c_floor = math.floor(c)

    if c_ceil == c_floor:
        return True
    else:
        return False

#Run through the possibility space
def poss_space():
    for a in range(1,499):
        for b in range(1,499):
            if has_int_root(a,b):
                c = int((a**2 + b**2)**0.5)
                if (a+b+c) == 1000:
                    print a
                    print b
                    print c
                    print a*b*c
                    return

poss_space()
                    

