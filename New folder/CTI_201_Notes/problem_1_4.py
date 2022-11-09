# Write a program that reads an integer number and 
# prints its previous and next numbers. See the example below.

# Understand:
# input: 
# num = int(input()) 
# output:
# next number & previous number 
# Match:
# simple arithmetic
# Plan:
# 1.get input
# 2.nextNum 
# 3.prevNum
# 4.print out 
# num = int(input())
# Implementation:
# 1.get input
num = int(input())
# 2.nextNum 
nextNum = "The next number for the number " + str(num) + " is "+str(num+1)
# 3.prevNum
prevNum = "\nThe previous number for the number " + str(num) + " is "+str(num-1)
# 4.print out 
print(nextNum, prevNum)

# Review:
# Evaluate #Time: o(1)