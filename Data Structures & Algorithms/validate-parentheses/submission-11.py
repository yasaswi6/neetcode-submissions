class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ['{', '[', '(']
        closing = ['}', ')', ']']

        for i in s:
            if i == '{' or i == '[' or i == '(':
                stack.append(i)
            else:
                if i == '}' and stack != []:
                    correct = stack.pop()
                    if correct != "{":
                        return False
                elif i == ']' and stack != []:
                    correct = stack.pop()
                    if correct != "[":
                        return False
                elif i == ')' and stack != []:
                    correct = stack.pop()
                    if correct != "(":
                        return False
                else:
                    return False
        if stack != []:
            return False
        return True
                


        