class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) -1
        
        maxarea = 0
        while i < j:
            height = min(heights[i], heights[j])
            if height * (j - i) > maxarea:
                maxarea = height * (j-i)
            elif heights[i] < heights[j]:
                i +=1
            else :
                j -= 1
        return maxarea
            
