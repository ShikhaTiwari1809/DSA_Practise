class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        def can_split(mid):
            allowed_days = 1
            weight_sum =0

            for w in weights:
                if weight_sum+w <=mid:
                    weight_sum+=w
                else:
                    allowed_days+=1
                    weight_sum =w
                    if allowed_days>days:
                        return False
            return True

        
        while low<=high:
            mid = (low+high)//2

            if can_split(mid):
                high = mid -1
            else:
                low = mid+1
        return low