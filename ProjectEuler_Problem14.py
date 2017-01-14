#Function to process a number in sequence and yield next number
def get_next_num(x):
    if x%2 == 0:
        return x/2
    else:
        return 3*x + 1

#Function to check million numbers
longest_sequence = 0
ls_starter = 0
    
for i in range(1,1000000):

    num = i

    sequence_length = 0

    while (num != 1):
        next_num = get_next_num(num)
        num = next_num
        sequence_length += 1

    if sequence_length > longest_sequence:
        longest_sequence = sequence_length
        ls_starter = i

    if i%10000 == 0:
        print i

print longest_sequence
print ls_starter
