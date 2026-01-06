from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m= len(s2)
        if n > m:
            return False

        s1cnt =[0]*26
        s2cnt =[0]*26
        base = ord('a')

        #count of s1 characters
        for ch in s1:
            s1cnt[ord(ch) - base] += 1
        
        for i in range(n):
            s2cnt[ord(s2[i]) - base]+=1
        
        if s1cnt == s2cnt:
            return True

        for r in range(n,m):
            s2cnt[ord(s2[r]) - base]+=1
            s2cnt[ord(s2[r-n]) - base]-=1
            if s1cnt == s2cnt:
                return True
        return False
