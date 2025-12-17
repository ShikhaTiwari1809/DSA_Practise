from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        element_cnt = Counter(nums)

        sorted_items_desc = dict(sorted(element_cnt.items(), key=lambda item: item[1], reverse=True))
        
        return(list(sorted_items_desc.keys())[:k])
        

        