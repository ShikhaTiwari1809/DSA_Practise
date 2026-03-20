class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) # nlogn
        longest = 0
        print(num_set)

        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(longest, length)

        return longest