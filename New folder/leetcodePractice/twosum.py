# U-Understand
# M-Match
# P-Plan
# I-Implement
# R-Review
# E-Evaulate

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
#https://zhenchaogan.gitbook.io/leetcode-solution/leetcode-1-two-sum

#1. go through the array add the element starting from the right 
#added by the next element ([i]+[i+1])

#check if the sum is equal to the target
#if it is return the indices
target = 9
nums = [2,7,11,15]
# nums = [3,2,4]
# nums = [3,3]
indices = []
for x in range(0, len(nums)):
    for y in range (x+1,len(nums)):
        sum = nums[x]+nums[y]
        if sum == target:
            indices.append(x)
            indices.append(y)
            break
print(indices)
# return indices

#double for loop
# Time Complexity: O(n^2)
# Space Complexity: O(1)

# def twoSum(nums, target):
#     #Initialize out list
#     out = []
#     #Loop through the input to pick first_num
#     for i in range(len(nums)):
#         first_num = nums[i];
#     #   Loop through the remaining input to pick sec_num
#         for j in range(i+1,len(nums)):
#             second_num = nums[j];
#     #       If (first_num+sec_num == target)
#             if (first_num + second_num == target):
#     #           Add index of first_num, sec_num to out
#                 out.append(i);
#                 out.append(j);
#     #Return out
#     return out;
    
# print(twoSum([2,3, 5, 7], 10));
# print(twoSum([2,3, 5, 7, 11], 10));