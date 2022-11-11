# Write a program that greets the user by printing the word "Hello", a comma, 
# the name of the user and an exclamation mark after it. See the examples below.

# Understand:
# input: Harry
# output: Hello, Harry!
# Match: concatinating
# Plan: 
# 1. get input
    # user_name = input()
# 2. concatinate 
    #  print(" Hello," + user_name + "!")
# Implementation:
# 1. get input
user_name = input()
# 2. concatinate 
print("Hello, " + user_name + "!")
# Review:
#test cases
# Evaluate #Time: 
# o(1)