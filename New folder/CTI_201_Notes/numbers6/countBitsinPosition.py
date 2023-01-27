# Given five input numbers, a, b, c, d and n,
# print out the number of 1 bits at the nth least 
# significant bit position in all four numbers a, b, c, d.

# Understand:
    # input: a,b,c,d,n : all int
    # output: print out amount of 1 bits total at the nth lsb position 
    
# Match:
    # bin() : int to binary
    # .split() : for input
    #  >> : move to the right 
    # %10 : get last digit
# Plan:
    #get inputs
    # shift right by n 
    # convert to bin
    # get last digit (either covert to decimal then %10 or [-1])
    #add digits
# Implementation:
#get inputs and put into a list 
list = input().split()
sum = 0 
# shift right by n 
# print(list)

# change to int 
# for i in range(0, len(list)):
#     list[i] = int(list[i])
#
# for i in range (0,len(list)-1):
#     print(bin(list[i]))

# print("___________________")

for i in range(0, len(list)-1):
    list[i] = int(list[i]) >> int(list[-1])
    sum = sum + int(bin(list[i])[-1]) 
    
# for i in range (0,len(list)-1):
#     print(bin(list[i]))
    
print(sum)
    

# print(list)


# convert to bin
# get last digit (either covert to decimal then %10 or [-1])
#add digits
# Review:
# Evaluate #Time: 