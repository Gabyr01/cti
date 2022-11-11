
# Days of week are numbered as: 0 — Sunday, 1 — Monday, 2 — Tuesday, 
# ..., 6 — Saturday.
# Understand:
# An integer K in the range 1 to 365 is given
# Find the number of day of week for K-th day
# of year provided that in this year January 1 was Thursday

# Match:
#%
# Plan:
# #input
# (input + 3) % 7 
# Implementation:
# #input
dayNumber = int(input())
startingDate = int(input())-1

print((dayNumber + startingDate) % 7 )
# Review:
# Evaluate #Time: 
