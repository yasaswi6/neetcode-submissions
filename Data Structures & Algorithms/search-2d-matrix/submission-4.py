class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix) - 1
        left = 0
        right = len(matrix[0]) -1
        while n >= 0:
            left = 0
            right = len(matrix[0]) -1
            while left <= right:
                mid = (left + right)//2
                if matrix[n][mid] == target:
                    return True
                elif target > matrix[n][mid]:
                    left = mid + 1
                else:
                    right = mid -1
            n -= 1
        return False
    

       
