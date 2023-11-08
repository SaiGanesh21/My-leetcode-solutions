class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        # if len(s)==1:
        #     return "a"
#         l=0
#         li=list(s)
#         r=len(s)-1
#         # t=r+1
#         while l<=r:
#             if s[l]==s[r]:
#                 # t-=2
#                 l+=1
#                 r-=1
#             elif s[l]!=s[r]:
#                 stor=min(s[l],s[r])
#                 li[l]=stor
#                 li[r]=stor
#                 l+=1
#                 r-=1
#         return "".join(li)
          n=len(s)
          s=list(s)
          for i in range(n//2):
             s[i],s[n-1-i]=min(s[i],s[n-1-i]),min(s[i],s[n-1-i])
          return "".join(s)
            
           
     
                # t-=2
                
                
                
                

                