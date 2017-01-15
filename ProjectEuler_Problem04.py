#Function to check if string is palindromic
def isPalindrome(string):
    for i in range(len(string)/2):
        if string[i] == string[-1-i]:
            pass
        else:
            return False
    return True

#Compute 3 digit number products in decreasing order
products = []

for i in range(999,99,-1):
    for j in range(999,99,-1):
        product = i*j
        if isPalindrome(str(product)):
            products.append(product)

print max(products)
            
        
        
