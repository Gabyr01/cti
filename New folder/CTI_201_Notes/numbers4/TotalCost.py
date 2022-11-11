# A cupcake costs A dollars and B cents. Determine how many dollars 
# and cents should one pay for N cupcakes. A program gets three numbers:
# A, B, N. It should print two numbers: total cost in dollars and cents.

# Understand:
#A program gets three numbers: A, B, N. 
# dollars, cents, cupcakeAmt
# print two numbers: total cost in dollars and cents.
# Match:
# Plan:
# 1. get inputs
# 2 calculate cents
    # cents = cent * cupcakeAmt
    # dollars = (dollars * cupcakeAmt) + (cents//100)
    # cents = cents % 100
#3 print output
# Implementation:
# 1. get inputs
dollars = int(input())
cent = int(input())
cupcakeAmt = int(input())

# 2 calculate cents
cents = cent * cupcakeAmt
dollars = (dollars * cupcakeAmt) + (cents//100)
cents = cents % 100
#3 print output
print(dollars,cents)
# Review:
# Evaluate #Time: 
