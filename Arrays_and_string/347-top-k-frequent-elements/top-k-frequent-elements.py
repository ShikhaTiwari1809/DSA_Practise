from collections import Counter,defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = Counter(nums)
        print(freq_count)
        sorted_freq = sorted(freq_count.items(), key=lambda item: item[1], reverse=True)
        print(sorted_freq[:k])
        ans = [i[0] for i in sorted_freq[:k] ]
        return ans

        