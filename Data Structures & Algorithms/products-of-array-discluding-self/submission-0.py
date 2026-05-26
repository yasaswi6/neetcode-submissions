class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        product = nums[0]
        for i in range(1,len(nums)):
            prefix.append(product)
            product *= nums[i]
            
        product = nums[len(nums)-1]
        suffix = [1]
        for i in range(len(nums)-2,-1,-1):
            suffix.append(product)
            product *= nums[i]
        result = []
        for i in range(0, len(nums)):
            result.append(prefix[i]*suffix[len(nums)-i-1])
        return result

            
