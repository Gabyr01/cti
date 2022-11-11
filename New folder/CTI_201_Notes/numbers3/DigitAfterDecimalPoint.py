
# Given a positive real number, print its first digit to
# the right of the decimal point without using string operations.

# Understand:
# input = float(input()) #real number

# Match:
# import math
# Plan:
# 1. digit = int(math.modf(input)*10)
# Implementation:
# import math
# input = float(input())
# fraction, whole = math.modf(input)
# print(int(fraction*10))

x = float(input())
x = x* 10
print(int(x%10))
# Review:
# Evaluate #Time: 
