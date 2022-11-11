
# Given a three-digit number. Find the sum of its digits without 
# using string operations.

# Understand:
#input = int(input()) #3 digit integer 
# Match:
# % && 10 
# Plan:s
#1. sum = 0
#2. while input > 0:
    # 483
        # digit = input % 10 # 3, 8, 4
        # sum = sum + digit # 3, 3 + 8, 11 + 4
        # input = input // 10 # 48, 4, 0     
#last step. print(sum)
# Implementation:
input = int(input()) #3 digit integer 
sum = 0 
while input > 0 :
    digit = input % 10
    sum = sum + digit 
    input = input // 10
    
print(sum)
    
# Review:
# Evaluate #Time: 
