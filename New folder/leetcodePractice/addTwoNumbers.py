
# l1 = [2,4,3]
# l2 = [5,6,4]
# l1 = [0]
# l2 = [0]
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
l3 = []
sum = 0
print("**********************")
maxInt = max(len(l1),len(l2))
minInt = min(len(l1),len(l2))
value1 = l1[i]
for i in range(maxInt):
    
    sum = sum + value1 +l2[i]
    remainder = 0
    if sum>=10:
        remainder = sum/10
        # print("hi: "+str(sum))
        
        sum = sum % 10
        
    l3.append(int(sum))
    sum = remainder
    if(i >= minInt):
        value=0
    
print(l3)