# Given the integer N - the number of minutes that is passed since 
# midnight - how many hours and minutes are displayed on the 24h 
# digital clock?

# The program should print two numbers: the number of hours 
# (between 0 and 23) and the number of minutes (between 0 and 59).

# For example, if N = 150, then 150 minutes have passed since midnight
# - i.e. now is 2:30 am. So the program should print 2 30.

# Understand:
# input = int(input()) # number of minutes that is passed since midnight
# print two numbers : hours minutes

# Match:
# Plan:
# 1. get input
# 2. hours = 150 // 60
# 3. minutes = 150 % 60
# 4. print
# Implementation:
# 1. get input
N = int(input())
# 2. hours = 150 // 60
hours = N // 60
# 3. minutes = 150 % 60
minutes = N % 60
# 4. print
print(hours, minutes)

# Review:
# Evaluate #Time: 
