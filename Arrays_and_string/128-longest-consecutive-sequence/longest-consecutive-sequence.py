class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = sorted(set(nums)) # nlogn
        
        ans = 1
        curr = 1

        if len(nums)==0:
            return 0

        for i in range(1,len(sett)):
            
            if sett[i-1] == sett[i]-1:
                curr +=1
            else:
                curr =1
            ans = max(ans,curr)
        
        return ans