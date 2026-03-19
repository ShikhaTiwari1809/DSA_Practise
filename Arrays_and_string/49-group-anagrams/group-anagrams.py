from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ch_map = defaultdict(list)
        
        for ch in strs:
            
            cur_key = tuple(sorted(ch))
            
            ch_map[cur_key].append(ch)
        
        return list(ch_map.values())
