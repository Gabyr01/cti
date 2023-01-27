
# 1. take input as int
# 2. extract LSB of both ints
# 3. compare the LSB 
# 4. print T/F

# user_input = input()
# list_user_input = user_input.split()

# Given two input numbers, print 'True' if the last least
# significant bit of the two number match and 'False' if they don't.

# Understand:
#   input:2 ints
#   output: true or false
# Match:
#   bit()#0b000
# Plan:
    # 1. take input as int
    # 2. extract LSB of both ints
    # 3. compare the LSB 
    # 4. print T/F
# Implementation:
a,b = input("enter two values: ").split()
a = bin(int(a))
b = bin(int(b))

if(a[-1]==b[-1]):
    print("True")
else:
    print("False")

# Review:
# Evaluate #Time: 