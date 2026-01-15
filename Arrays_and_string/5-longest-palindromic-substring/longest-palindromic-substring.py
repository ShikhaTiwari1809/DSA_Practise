class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start = end = 0  # inclusive indices of best palindrome

        def expand(l: int, r: int) -> tuple[int, int]:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # went 1 step too far on both sides
            return l + 1, r - 1

        for i in range(len(s)):
            # odd length palindrome
            l1, r1 = expand(i, i)
            if r1 - l1 > end - start:
                start, end = l1, r1

            # even length palindrome
            l2, r2 = expand(i, i + 1)
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]
