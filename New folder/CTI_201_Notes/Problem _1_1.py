#understand:
# 3 inputs -> assume all are int? 
# match:
# basic arithmentic
#plan:
#1. get 3 inputs
#2. add to the sum 
#3. after you get the total sum you print the output 
#note; forloop? 3 times. 
#implement 
sum  = 0 
for x in range(3):
    user_input = int(input())
    sum = sum + user_input
print(sum)
#results
#Evaluate 
#O(n)
    