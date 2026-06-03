class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for i in range(len(s)-1,-1,-1):
            if s[i].isalnum():
                result+=s[i]
        normal = ""
        for i in s:
            if i.isalnum():
                normal += i
        print(result)
        print(normal)
        if normal.lower() == result.lower():
            return True
        return False
        
        