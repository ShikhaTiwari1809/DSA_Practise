# https://leetcode.com/problems/maximum-sum-circular-subarray/
# Good explanation: https://algo.monster/liteproblems/918

# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

# Example 1:

# Input: nums = [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3.
# Example 2:

# Input: nums = [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
# Example 3:

# Input: nums = [-3,-2,-3]
# Output: -2
# Explanation: Subarray [-2] has maximum sum -2.
 

def circularKadence(nums):
    globalMax,globalMin = nums[0], nums[0]
    total =0
    curMax, curMin =0,0

    for n in nums:
        curMax = max(curMax+n,n)
        curMin = min(curMin+n,n)

        total+= n

        globalMax = max(globalMax,curMax)
        globalMin = min(globalMin,curMin)
    if globalMax>0:
        return max(globalMax,total-globalMin)
        
    else:
        return globalMax
        
nums = [1,-2,3,-2]
maxSum = circularKadence(nums)
print(maxSum)

nums = [5,-3,5]
maxSum = circularKadence(nums)
print(maxSum)


nums = [-3,-2,-3]
maxSum = circularKadence(nums)
print(maxSum)