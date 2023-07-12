class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for x in s:
            if stack and x=="*":
                stack.pop()
            else:
                stack.append(x)
        return ''.join(stack)
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         ans=[]
#         for i in s:
#             if i=='*':
#                 del ans[-1]
#                 # print(a)
                
#             else:
#                 ans.append(i)
#         return "".join(ans)
        ans=[]
        for i in s:
            if i=='*':
                a=ans.pop(-1)
                print(a)
            else:
                ans+=[i]
        return "".join(ans)
       