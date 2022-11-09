#171. Excel Sheet Column Number
# Given a string columnTitle that represents the column title as appears
# in an Excel sheet, return its corresponding column number.
# For example:
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...


# 1. convert letter to number
    #letter+1 - 'A' = number
# simplify what if the input is 1 char?
#2 characters ?? 
#    current = remainder % 26
#>>> print(ord('c')-ord('a'))



# def columnNumber(letter):
#     sum = 0
#     MAX = len(letter)
#     for i in range(MAX):
#         s = letter[-(i+1)]
#         print( s)
#         # letter = letter[:-1]
#         num = ord(s) - ord('A')
#         num = int(num+1)
#         sum = sum + (26**i *num)
        
#     return sum
        
def columnNumber(letter):
    result = 0
    for i in letter:
        # s = letter[-(i+1)]
        # print( s)
        # letter = letter[:-1]
        num = ord(i) - ord('A')
        num = int(num+1)
        result = result *26+num
        
    return result
    
print(columnNumber('AAC'))