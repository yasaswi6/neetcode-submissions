class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        # Step 1: binary search on rows
        top = 0
        bottom = rows - 1
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] <= target <= matrix[mid][cols - 1]:
                # target falls in this row's range
                break
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                top = mid + 1
        else:
            return False  # no valid row found

        # Step 2: binary search within that row
        row = mid
        left = 0
        right = cols - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                right = mid - 1

        return False