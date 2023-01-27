# Given two input numbers, print out the two numbers
# with their binary value shifted to the right by 1 bit.


# Understand:
    # input : int a , int b 
    # output : binary value shifter to the right by 1 bit
# Match:
    # bin() , int to binary
    # >> , shift to the right
    #.split , split 2 inputs
# Plan:
    # get inputs
    # change to binary
    #shift to the right by 1 bit 
# Implementation:
    # get inputs
a,b = input().split()
    # change to binary
# a = bin(int(a))
# b = bin(int(b))
    #shift to the right by 1 bit 
# a = a[2:]
# b = b[2:]

print(int(a)>>1, int(b)>>1)

# Review:
# Evaluate #Time: 
