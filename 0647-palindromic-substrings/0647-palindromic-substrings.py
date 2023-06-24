class Solution:
    def countSubstrings(self, s: str) -> int:
        ans=0
        def sub(s,l,r):
            res=0
            while l>=0 and r<len(s) and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
            return res
        for i in range(len(s)):
            ans+=sub(s,i,i+1)
            ans+=sub(s,i,i)
        return ans


        
            
        
            
        