class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels =['a','e','i','o','u']
        max_cnt = 0
        cur_max =0
        
        s_list = list(s)
        
        for i in range(0,k):
            if s_list[i] in vowels:
                max_cnt+=1
        
        cur_max =max_cnt
        
        for i in range(k,len(s_list)):
            if s_list[i] in vowels:
                cur_max+=1
            if s_list[i-k] in vowels:
                cur_max-=1
            max_cnt = max(max_cnt, cur_max)
        
        
        return max_cnt

        