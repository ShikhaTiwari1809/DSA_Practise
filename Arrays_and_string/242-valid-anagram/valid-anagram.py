from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = [0]*26
        countT = [0]*26

        for ch in s:
            countS[ord(ch)-ord('a')]+=1
        
        for ch in t:
            countT[ord(ch)-ord('a')]+=1
        
        return countS == countT