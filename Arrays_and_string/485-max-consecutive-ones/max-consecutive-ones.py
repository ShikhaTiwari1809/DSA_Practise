class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        current_cnt = 0
        for i in nums:
            
            if i == 1:
                current_cnt+=1
            else:
                cnt = max(current_cnt,cnt)
                current_cnt = 0
            
        
        return max(current_cnt,cnt)