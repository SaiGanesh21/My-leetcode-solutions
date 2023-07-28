class Solution:
    def minSwaps(self, s: str) -> int:
        stack=[]
        for x in s:
            if stack and stack[-1]=="[" and x=="]":
                stack.pop()
            else:
                stack.append(x)
        print(stack)
        if len(stack)==2:
            return 1
        elif len(stack)>2:
            return ((len(stack)//2)+1)//2
        else:
            return 0
        