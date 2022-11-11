#Given two timestamps of the same day: a number of hours, minutes and 
# seconds for both of the timestamps. The moment of the first 
# timestamp happened before the moment of the second one. 
# Calculate how many seconds passed between them.

# Understand:
# input: 6 total: first 3 = 1st timestamp : next 3 = 2nd timestamp 
# output: how many seconds passed between them 
# Match: modulus 
# Plan: 
# 1. get inputs
# 2. convert to seconds
# 3. subtract to get difference
# 4. output
# Implementation:
# 1. get inputs
# 2. convert to seconds
hours = int(input())*60*60
minutes = int(input())*60
seconds = int(input())
sum = hours+minutes+seconds

hours2 = int(input())*60*60
minutes2 = int(input())*60
seconds2 = int(input())
sum2 = hours2+minutes2+seconds2
# 3. subtract to get difference
difference = sum2 - sum

# 4. output
print(difference)
# Review:
# Evaluate #Time: O(1)