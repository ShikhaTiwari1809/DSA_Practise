from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        element_cnt = Counter(nums)
        #print(element_cnt)
        sorted_items_desc = sorted(element_cnt.items(), key=lambda item: item[1], reverse=True)
        sorted_dict_desc = dict(sorted_items_desc)
        return(list(sorted_dict_desc.keys())[:k])
        

        