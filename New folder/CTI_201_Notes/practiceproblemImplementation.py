# Understand #input and output #big example/test case
# Match #What category does this problem remind me of?
# Plan #Criteria: 
    # Use a function to encapsulate your pseudo code
    # Keep it simple and concise
    # Use logical indentation and white space
    # Use good naming conventions
    # Don’t be too abstract 
# Implementation
# Review #Variables & expressions to track: 
# Evaluate #Time: O(n)
        #Space: O(n)

#U
# input: 2 numbers
# monthlySpent =int() how much someone spends a month
# monthlyEarned =int() how much someone earns a month
#M this reminds me of simple arithmetic 
#P 
# 1. get inputs
# 2. spendingRate = (monthlySpent/ monthlyEarned) * 100
# 3. savingRate = 1-(spendingRate/100)
# 4. print output
#I
#
#R
#E
#o(1) - linear


# 1. get inputs
monthlySpent = int(input())#36000
monthlyEarned = int(input())#100000

# 2. spendingRate = (monthlySpent/ monthlyEarned) * 100
spendingRate = (monthlySpent/monthlyEarned) *100 #36.0

# 3. savingRate = 100-spendingRate
savingRate = 100-spendingRate #64.0

# 4. print output
print("Your spending rate is %s %s and your savings rate is %s %s" %(str(spendingRate),"%", str(savingRate), "%"))

