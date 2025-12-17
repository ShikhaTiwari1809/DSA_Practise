from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams_map=defaultdict(list)

        for word in strs:
            sorted_key=tuple(sorted(word))

            anagrams_map[sorted_key].append(word)
        return list(anagrams_map.values())