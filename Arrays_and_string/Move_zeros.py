""" https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=leetcode-75
 Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0] """

""" In this as we can see we can utilize two pointer pattern here we can have l and r and then compare both of them
say if l and r both are zero then just increment r as we have correct 
but if say l is zero but r is not we need to swap l with r value and replace r with zero. """

def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    l=0
    r=1
    while r < len(nums):
        if nums[l]==0 and nums[r]==0:
            r+=1
        elif nums[l]==0 and nums[r]!=0 :
            nums[l]=nums[r]
            nums[r]=0
            l+=1
            r+=1
        else:
            l += 1
            r += 1

    print(nums)

nums = [0,1,0,3,12]
moveZeroes(nums)
        