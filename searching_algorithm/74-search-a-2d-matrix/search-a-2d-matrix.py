class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m =len(matrix)
        n = len(matrix[0])
        total = m*n
        
        l =0
        r = total-1
        while l<=r:
            m= (l+r)//2
            i = m//n
            j = m % n
            middle_element = matrix[i][j]
            if middle_element==target:
                return True
            elif target< middle_element:
                r=m-1
            else:
                l=m+1
        return False



        