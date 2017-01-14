#Factorial function
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)

#Computer can give the answer directly, so no complex algorithm
num = fact(100)
str_digs = str(num)
list_digs = [int(dig) for dig in str_digs]
print sum(list_digs)
