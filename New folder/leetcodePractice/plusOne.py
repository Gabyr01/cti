
        # input: large integer array []
        # output: add 1 to the large integer 
        
        # 1. get input
        # 2. get the last index 
        # 3. add 1 to the last index value (sum)
        # if (sum == 10 )
        #   get 2nd to last digit and add 1
        # 4. return array 
        #steps 2-3 will be repeated, lastindex will become 2nd to last, 3rd to last, etc
        
digits = [1,2,3]

for i in range(1, len(digits)+1):
    # print(digits)
    currentElement = digits[-i] + 1 #currentElement is the element starting from the last to first element in the array        
    
    if(currentElement >= 10):
        digits[-i] = 0
        # print(digits[-i])
        # print(i)
        if(len(digits)-i == 0 ):
            # print(i)
            if(i == len(digits)):
                i = 1
            digits = [i] + digits
            # print("hello")
            break
    else:
        digits[-i] = digits[-i] + 1
        break
                        
print(digits)

#O(1)

# def plusOne(digits):
#     #Set i to length of digits - 1
#     i = len(digits) - 1;
#     #Initialize a out list
#     out = []
#     #Calculate temp = digits[i] + 1
#     temp = digits[i] + 1
#     while(True):
#         #If (temp == 10)
#         #  Insert 0 on the top of out
#         #  Set carry = 1
#         #Else
#         # Insert temp on the top of out
#         # Set carry = 0
#         if (temp == 10):
#             out.insert(0, 0);
#             carry = 1;
#         else:
#             out.insert(0, temp);
#             carry = 0;
#         #Decrement i
#         i = i - 1;
#         #If (i < 0):
#         #   Exit from loop
#         if (i < 0):
#             break;
#         #Calculate temp = digits[i] + carry
#         temp = digits[i] + carry;
#     #Go back to 4
#     return out;
# input_list = [9, 9, 9, 9]    
# output = plusOne(input_list);
# print (output);