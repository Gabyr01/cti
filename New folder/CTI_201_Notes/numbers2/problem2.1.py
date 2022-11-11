# Purpose: Practice two-bit integer problems
# Problem Statement: Given a 2 bit integer, print its left bit 
# (a 2's bit) and then its right bit (a ones bit). Use the operator 
# of integer division for obtaining the 2's bit and the operator of 
# taking remainder for obtaining the ones bit.

# Understand:
# input: decimal number
# output: 2 bit integer 
# Match: modulus
# Plan:
# 1. get input 
# 2. left bit : userInput//2
# 3. right bit: userInput%2
# 4. print 2 bit
# Implementation:
# 1. get input 
userInput = int(input())
# 2. left bit : userInput//2
left = userInput//2
# 3. right bit: userInput%2
right = userInput%2
# 4. print 2 bit
print(str(left) +" "+ str(right))
# Review:
# Evaluate #Time: 
# O(1)

