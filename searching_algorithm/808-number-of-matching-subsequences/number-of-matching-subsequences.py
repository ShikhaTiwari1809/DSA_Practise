from collections import defaultdict, deque
from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(deque)

        # Put each word into the bucket of its first needed character
        for w in words:
            waiting[w[0]].append((w, 0))  # (word, index of next char to match)

        ans = 0

        for ch in s:
            bucket = waiting[ch]
            waiting[ch] = deque()  # clear; we'll refill with advanced states

            while bucket:
                w, i = bucket.popleft()
                i += 1  # matched this char
                if i == len(w):
                    ans += 1
                else:
                    waiting[w[i]].append((w, i))

        return ans
