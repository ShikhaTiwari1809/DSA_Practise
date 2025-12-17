from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = defaultdict(list)
        for st in strs:
            
            #cur_key = ''.join(sorted(st))
            cur_key = tuple(sorted(st))
            ans[cur_key].append(st)

 
        return list(ans.values())
