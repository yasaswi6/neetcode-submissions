class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ["*", "+", "-", "/"]:
                stack.append(i)
            elif i == "+":
                second = stack.pop()
                first = stack.pop()
                result = int(first) + int(second)
                stack.append(result)
            elif i == "-":
                second = stack.pop()
                first = stack.pop()
                result = int(first) - int(second)
                stack.append(result)
            elif i == "/":
                second = stack.pop()
                first = stack.pop()
                result = int(first) / int(second)

                stack.append(result)
            elif i == "*":
                second = stack.pop()
                first = stack.pop()
                result = int(first) * int(second)
                stack.append(result)
        return int(stack.pop())
        
            
            

        