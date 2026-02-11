class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        if n-k ==0:
            return sum(cardPoints)
        
        # start by taking all k from the left
        left_sum = sum(cardPoints[:k])
        best = left_sum
        right_sum = 0

        # move 1 card at a time from left end to right end
        for i in range(1, k + 1):
            left_sum -= cardPoints[k - i]      # remove one from the left-picked set
            right_sum += cardPoints[-i]        # add one from the right end
            best = max(best, left_sum + right_sum)

        return best



        