# Given an integer greater than 9, print a new number that has the two digits 
# in the reverse order, 1's value first, and then 10's value.
# Understand:
# input: int > 9
# output  last two digits in the reverse order,
# Match:
# % & //
# Plan:
# 1. get input 
# 2. get last 2 digits : %100
# 3. get left digit: //10
# 4. get right digit: % 3 
# 5. print(right + left)
# Implementation:
# Plan:
# 1. get input 
num = int(input())
# 2. get last 2 digits : %100
lastTwoDigit = num % 100
# 3. get left digit: //10
left = lastTwoDigit // 10
# 4. get right digit: % 10
right = lastTwoDigit % 10 
#5
newValue = (right * 10) + left
print(newValue)
# Review:
# Evaluate #Time: 