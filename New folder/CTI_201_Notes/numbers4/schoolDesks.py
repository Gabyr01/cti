# A school decided to replace the desks in three classrooms. Each desk sits two students. 
# Given the number of students in each class, 
# print the smallest possible number of desks that can be purchased.

#The program should read three integers: 
# the number of students in each of the three classes, a, b and c respectively.


# Understand:
#input -> 3 integers : the number of students in classes a,b,c
#output -> smallest possible number of desks that can be purchased
#test case ->
#            input     |   amt desks   |  output
# class a: 20 students | 10 desks      |   32
# class b: 21 students | 11 desks min  |
# class c: 22 students | 11 desks      |

# Match: mod to check if number is even 
#        division 
# Plan:
# input = input()
# if (odd)
#   output = input / 2 + 1 
# output = input / 2
#   
# Implementation:
# a, b, c  = input()
classrooms = []
totalDesks = 0 
for x in range(3):
    classrooms.append(int(input()))

for x in classrooms:
    if(x%2==1): # if odd
        desksNeeded = int(x / 2) + 1 #round up
    else:
        desksNeeded = int(x / 2)
    totalDesks = totalDesks + desksNeeded
print(totalDesks)
# Review:
# Evaluate #Time: 