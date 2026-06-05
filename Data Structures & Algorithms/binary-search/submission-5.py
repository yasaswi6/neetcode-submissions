class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1
        n = (left + right+1)//2
        while left <= right:
            if(nums[n] == target):
                return n
            elif target > nums[n]:
                left = n +1
                n = (left + right)//2
        
            else:
                right = n-1
                n = (left + right)//2
        return -1


        