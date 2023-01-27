# Understand:
# Write a program that takes a single upper case letter as 
# input and prints its position number in alphabet sequence.
#input: uppercase letter -> datatype: char 
#output: alphabet sequence -> datatype: int

# Match: 
#ASCII table
#A = 65, Z = 98
#>>> ord("a")
# 97
# >>> chr(97)
# 'a'

# Plan:
#1. get the char input
    #1.5 make sure its an uppercase char
#2. convert char to int thenA
# subtract 65 from the input and add 1 
#3. print out the int
 
# Implementation:
#1. get the char input
# upperChar = chr(input())
#while 
    #1.5 make sure its an uppercase char
# Review:
# Evaluate #Time: y


upperChar = str(input())
while not (upperChar.isupper() and len(upperChar)==1):
    upperChar = input()
position = ord(upperChar)-64 #-65 + 1
print(position) 



