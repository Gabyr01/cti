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