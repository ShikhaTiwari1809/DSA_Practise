class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l =0
        r =len(nums)-1

        ans =0
        nums.sort()
        while l<r:
            summ = nums[l]+nums[r]
            if summ == k:
                ans+=1
                l+=1
                r-=1
            elif summ>k:
                r-=1
            else:
                l+=1
        return ans