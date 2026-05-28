class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        length = 1
        values = {}
        for i in range(len(nums)):
            if nums[i] not in values:
                values[nums[i]]=0
       
        fv = min(values.keys())
        count = fv
        sq ={fv:1}
        for i in range (len(values)):
            values.pop(count)
            if count + 1 in values.keys():
                count +=1
                sq[fv] = sq[fv] +1                 
            elif values:
                fv = min(values.keys())
                sq[fv] = 1
                count = fv
        
        return max(sq.values())





        