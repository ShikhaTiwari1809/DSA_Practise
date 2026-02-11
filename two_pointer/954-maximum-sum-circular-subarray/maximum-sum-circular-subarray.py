class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        
        # For max subarray (Kadane)
        curr_max = best_max = nums[0]
        
        # For min subarray (Kadane variant)
        curr_min = best_min = nums[0]
        
        
        
        for x in nums[1:]:
            
            curr_max = max(x, curr_max + x)
            best_max = max(best_max, curr_max)
            
            curr_min = min(x, curr_min + x)
            best_min = min(best_min, curr_min)
        
        # If all numbers are negative, best_max is the answer
        if best_max < 0:
            return best_max
        
        return max(best_max, total - best_min)

        