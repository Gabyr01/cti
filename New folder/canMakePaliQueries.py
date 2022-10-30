queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
s = "abcda"
list = []
#1 get the first index of the query 

for i in range(len(queries)):
    print("query: " + str(i))
    startSS = int(queries[i][0]) 
    
    endSS = queries[i][1] + 1 
    replaceAmt = queries[i][2] 
    
    string =s[startSS:endSS]
    print("string: " + string)
    half = int(len(string)/2)
    
    print("half= " + str(half))
    L =  string[0:half]
    R =  string[-(half):]
    #replace the amt possible 
    # print(L)
    print(L)
    print(R)
    print(replaceAmt)
    if(half == 0):#means just a single letter
        print("palindrome")
        list.append("true")
    elif L == R:
        print("palindrome")
        list.append("true")
    else:
        count = 0
        for i in range(1, half):
            L_char = L[i-1:i]
            R_char = R[-i:len(R)-(i-1)]
            
            if(L_char == R_char):
                count= count+1
                
        if(count>=0 and count< replaceAmt):
            print("palindrome")
            list.append("true")
        else:
            print("not palindrome")
            list.append("false")
   
        
print(list)            
    # print(R)
    #check if palindrom
    #start at the left L
    #compare to the right R
    
#check if palindrome
# print(len(queries[0]))
########################
# queries[i] = [lefti, righti, ki]
# Input: s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
# Output: [true,false,false,true,true]
#1 break up the queries
#2 create a substring from query 
#3 replace k letters in substring 
#4 is palindrome