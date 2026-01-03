class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarySearch(nums,target,leftBias):
            l =0
            r=len(nums)-1
            i=-1

            while l<=r:
                mid = (l+r)//2
    
                if target<nums[mid]:
                    r=mid-1
                elif target>nums[mid]:
                    l=mid+1
                else:
                    i=mid
                    if leftBias:
                        r=mid-1
                    else:
                        l=mid+1
            return i
        
        left = binarySearch(nums,target,True)
        right = binarySearch(nums,target,False)
        return [left,right]

        
        