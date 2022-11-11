# Given an integer greater than 9, print all the digits in the 
# reverse order, 1's value first, and then 10's value and then 
# the 100's value, and so on, with a space in between.

# Understand:
# input = int(input)
# output -> print(inReverseOrder)
# Match:
# 1234
# 4 3 2 1 
# get last digit: input%10 = 1
# output = str(lastDigit)

# for i inRange(1, len(input))

#   currentNum = input // 10**i
#   digit = currentNum % 10
#   output = output + str(digit)
# 
# Plan:
# loop 
    # 1. get the last digit -> digit = input%10
    # 2. add digit to output string  -> output = output + str(digit)
    # 3. get newNum without the prev last digit -> input = input // 10 
#outside of loop
    #4. print the output
# Implementation:
input = int(input())
output = ""

for i in range(1, len(str(input))+1):
    digit = input%10
    output = output +str(digit)+ " "
    input = input //10 
    
print(output)
# Review:
# Evaluate #Time: 
