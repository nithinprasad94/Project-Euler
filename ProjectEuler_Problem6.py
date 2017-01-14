#1) Sum of squares of first 100 Natural numbers
squares = [i*i for i in range(101)]
sum_squares = sum(squares)
print sum_squares

#2) Square of sum of first 100 Natural numbers
sum_nums = sum(range(101))
square_sum = sum_nums**2
print square_sum

#3) Difference
diff = square_sum - sum_squares
print diff
