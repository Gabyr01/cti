# N students take K apples and distribute them among each other evenly. 
# The remaining (the indivisible) part remains in the basket. 
# How many apples will each single student get? 
# How many apples will remain in the basket?

# Understand:
# 2 inputs: int() 
# students
# apples
# output: int()
# distribute = amt distributed to each student
# remainder = apples%students
# Match:modulus
# Plan:
# 1. get both inputs
# 2. calculate amt distributed evenly
# 3. calc remainder
# 4. print 2 & 3
# Implementation:
# 1. get both inputs
students = int(input())
apples = int(input())
# 2. calculate amt distributed evenly
distribute = int(apples/students)
# 3. calc remainder
remainder = apples%students
# 4. print 2 & 3
print(distribute)
print(remainder)

# Review:
# Evaluate #Time: O(1)