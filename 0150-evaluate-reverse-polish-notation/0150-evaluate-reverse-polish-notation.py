class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for x in tokens:
            if x in "+-/*":
                if x=="+":
                    s=stack.pop(-2) + stack.pop(-1)
                    stack.append(s)
                if x=="-":
                    s=stack.pop(-2) - stack.pop(-1)
                    stack.append(s)
                if x=="/":
                    s=stack.pop(-2)/stack.pop(-1)
                    stack.append(int(s))
                if x=="*":
                    s=stack.pop(-2)*stack.pop(-1)
                    stack.append(s)    
            else:
                stack.append(int(x))
        return stack[-1]