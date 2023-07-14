class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        for x in s:
            if x =="(":
                stack.append(0)
            else:
                if stack[-1]==0:
                    stack.pop()
                    stack.append(1)
                else:
                    val=0
                    while stack[-1]!=0:
                        val+=stack.pop()
                    stack.pop()
                    stack.append(2*val)
        return sum(stack)
                    
                    
                    
 
  