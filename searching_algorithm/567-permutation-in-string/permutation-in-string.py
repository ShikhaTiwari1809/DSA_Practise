from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        l =0
        r = l+window
    
        s2list = list(s2)
        s1list = list(s1)
        while r<=len(s2list):
            
            if set(s1list) == set(s2list[l:r]):
                if Counter(s1list)==Counter(s2list[l:r]):
                    return True
            
            r +=1
            l +=1
        return False


        