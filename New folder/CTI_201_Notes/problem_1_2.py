# Problem: Write a program that reads the length of the base and the height of a right-angled triangle and prints the area. Every number is given on a separate line.
# Understand:
# 2 inputs: both int()
# 1st: base = int(input())
# 2nd: height = int(input())
# output: base*height*(1/2) #float
# Match:
# basic arithmentic
# Plan:
# 1. get inputs
# 2. compute equation
# 3. output the area
# Implementation:
# 1. get inputs
base = int(input())
height = int(input())
# 2. compute equation
area = base*height*(1/2)
# 3. output the area
print(area)
# Review:
# test base case
# Evaluate #Time: 
# o(1)

