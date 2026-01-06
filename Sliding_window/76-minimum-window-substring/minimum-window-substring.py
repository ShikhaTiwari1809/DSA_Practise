from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(t) > len(s):
            return ""

        need = Counter(t)                 # counts needed
        window = defaultdict(int)         # counts in current window

        required = len(need)              # number of distinct chars needed
        formed = 0                        # how many distinct chars currently satisfied

        l = 0
        best_len = float("inf")
        best_l = 0

        for r, ch in enumerate(s):
            window[ch] += 1

            # if this char is required and we just met its needed count
            if ch in need and window[ch] == need[ch]:
                formed += 1

            # try to shrink while valid
            while formed == required and l <= r:
                window_len = r - l + 1
                if window_len < best_len:
                    best_len = window_len
                    best_l = l

                left_ch = s[l]
                window[left_ch] -= 1
                if left_ch in need and window[left_ch] < need[left_ch]:
                    formed -= 1
                l += 1

        return "" if best_len == float("inf") else s[best_l: best_l + best_len]
