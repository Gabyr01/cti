# Problem Statement:
# Given an integer, print its tens digit.

# Understand:
# integer = int(input())
# print(10's digit)

# Match:
#%
# //
# Plan:
# 1. get input
# 2. get last 2 digits -> input = input % 100
# 3. get 10's place -> tensPlace = input // 10 
# 4. print(tensPlace)
# Implementation:
# 1. get input
integer = int(input())
# 2. get last 2 digits -> input = input % 100
integer = integer % 100
# 3. get 10's place -> tensPlace = input // 10 
tensPlace = integer // 10 
# 4. print(tensPlace)
print(tensPlace)
# Review:
# Evaluate #Time: 
