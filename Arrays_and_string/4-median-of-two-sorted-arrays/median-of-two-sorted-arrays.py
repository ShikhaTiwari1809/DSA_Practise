import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 =l2=0
        final_num = []

        while l1<len(nums1) and l2<len(nums2):
            
            if nums1[l1]<=nums2[l2]:
                final_num.append(nums1[l1])
                l1+=1
            else:
                final_num.append(nums2[l2])
                l2+=1
    
        # add leftovers (flat)
        final_num.extend(nums1[l1:])
        final_num.extend(nums2[l2:])


        return statistics.median(final_num)