class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        max_L = [0]*n
        max_R = [0]*n
        left_wall = 0
        right_wall = 0

        for i in range(n):
            j =-i-1
            max_L[i] = left_wall
            max_R[j] = right_wall
            left_wall = max(left_wall, height[i])
            right_wall = max(right_wall,height[j])
        
        summ =0 
        for i in range(n):
            capacity = min(max_L[i],max_R[i])
            summ += max(0,capacity-height[i])
        return summ