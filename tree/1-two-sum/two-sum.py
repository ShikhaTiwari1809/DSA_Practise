class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapp = defaultdict()
        for i, num in enumerate(nums):
            
            alternate = target - num
            if alternate in mapp.keys():
                return [mapp[alternate],i]
            mapp[num] = i 
