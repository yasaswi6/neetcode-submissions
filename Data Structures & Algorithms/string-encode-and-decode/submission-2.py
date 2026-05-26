class Solution:

    def encode(self, strs: List[str]) -> str:
        answer = ""
        for value in strs:
            value = str(len(value))+"#"+value
            answer += value
        print(answer)
        return  answer    
    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        nums = ["0","1","2","3","4","5","6","7","8","9"]
        read = ""
        while i < len(s):
            
            if(s[i] in nums):
                read += s[i]
            if(s[i] == "#"):
                join = ""
                for i in range(i+1,i+1+int(read)):
                    join += s[i]
                result.append(join)
                
                read = ""
            i +=1
        print(result)
        return result

