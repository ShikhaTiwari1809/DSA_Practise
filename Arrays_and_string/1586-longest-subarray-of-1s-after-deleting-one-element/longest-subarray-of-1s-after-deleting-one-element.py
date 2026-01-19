class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k =1
        left = 0
        max_sum = 0
        num_delete = 0
        for right in range(len(nums)):
            if nums[right]==0:
                num_delete +=1
            if num_delete>k:
                if nums[left] ==0:
                    num_delete-=1
                left+=1
        
        return len(nums) - left -1