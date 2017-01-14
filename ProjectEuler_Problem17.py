#Number-to-Text Converter Function
def num_to_text(num):

    constants = {}
    constants['1'] = 'one'
    constants['2'] = 'two'
    constants['3'] = 'three'
    constants['4'] = 'four'
    constants['5'] = 'five'
    constants['6'] = 'six'
    constants['7'] = 'seven'
    constants['8'] = 'eight'
    constants['9'] = 'nine'
    constants['10'] = 'ten'
    constants['11'] = 'eleven'
    constants['12'] = 'twelve'
    constants['13'] = 'thirteen'
    constants['14'] = 'fourteen'
    constants['15'] = 'fifteen'
    constants['16'] = 'sixteen'
    constants['17'] = 'seventeen'
    constants['18'] = 'eighteen'
    constants['19'] = 'nineteen'
    constants['20'] = 'twenty'
    constants['30'] = 'thirty'
    constants['40'] = 'forty'
    constants['50'] = 'fifty'
    constants['60'] = 'sixty'
    constants['70'] = 'seventy'
    constants['80'] = 'eighty'
    constants['90'] = 'ninety'
    constants['100'] = 'hundred'
    constants['1000'] = 'thousand'

    units = str(num%10)
    rest = num - int(units)
    tens = str(rest%100)
    rest = rest - int(tens)
    hundreds = str(rest%1000)
    num_hundreds = str((rest/100)%10)
    rest = rest - int(hundreds)
    if num_hundreds != '0':
        hundreds = str(int(hundreds)/int(num_hundreds))
    thousands = str(rest%10000)
    num_thousands = str(rest/1000)
    if num_thousands != '0':
        thousands = str(int(thousands)/int(num_thousands))

    str_list = []

    if thousands != '0':
        str_list.append(constants[num_thousands])
        str_list.append(constants[thousands])

    if hundreds != '0':
        str_list.append(constants[num_hundreds])
        str_list.append(constants[hundreds])

    if hundreds != '0' and (tens != '0' or units != '0'):
        str_list.append('and')

    if tens != '0':
        if tens == '10':
            new_str = str(int(tens) + int(units))
            str_list.append(constants[new_str])

        else:
            str_list.append(constants[tens])

    if units != '0' and tens != '10':
        str_list.append(constants[units])

    #NOTE: we didn't use hyphen here ...
    
    return str_list

#Main Program
running_length = 0

for i in range(1,1001):
    str_list = num_to_text(i)
    print str_list
    str_joined = "".join(str_list)
    running_length += len(str_joined)

print running_length


        
        
    
    
