# Questions: 
# Given the integer N - the number of seconds that is passed since midnight 
# - how many full hours and full minutes are passed since midnight?
# Understand:
# input: in seconds : int()
# seconds = input()
# output: fullHours fullMin
# Match: use // 
# Plan:
# 1. get input
# 2. calc fullHours
# 60 secs * 60 mins = 3600 seconds = 1 hour
    # fullHours = seconds / 3600
# 3, calc fullMin
    # fullMin = seconds/60
# print out 
# Implementation:
# 1. get input
seconds = int(input())
# 2. calc fullHours
# 60 secs * 60 mins = 3600 seconds = 1 hour
fullHours = seconds // 3600
# 3, calc fullMin
fullMin = seconds //60
# print out 
print(fullHours, fullMin)
# Review:
# Evaluate #Time: O(1)