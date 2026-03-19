class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            if target - nums[i] in seen.keys():
                print(seen)
                return [i, seen[target - nums[i]]]
            seen[nums[i]] = i
        print(seen)
        return False