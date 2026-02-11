class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = best_sum = nums[0]
        
        for x in nums[1:]:
            curr_sum = max(x, curr_sum + x)
            best_sum = max(best_sum, curr_sum)
        
        return best_sum