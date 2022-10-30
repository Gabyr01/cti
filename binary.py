


#print
print("Enter your bill amount: ")
#base system  
a = int(float(input()))
print("base number system: ")
base = int(float(input()))
remainder = a
power = 0
#10 spaces are reserved 
#printed on the left side <
#printed on the right side >
#formating a print out 
print(f"{str(base)+'^i ':<4}{'| sum ': <10}{'| amt_needed':<10}")
decimal = 0
while remainder != 0:
    current = remainder % base
    print( f"{str(power).center(5):<5}{'| '+str(base**power):<10}{'| '+str(current):<10}")
    decimal = int(decimal) + ((base**power) * int(current))
    
    power+=1
    remainder = remainder//base

print("total: " + str(int(decimal)))
print((base**power) * current)