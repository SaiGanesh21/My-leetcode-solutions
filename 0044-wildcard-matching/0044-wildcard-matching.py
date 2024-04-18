class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def isallstars(p,j):
            for j1 in range(j+1):
                if p[j1]!="*":
                    return False
            return True
        n=len(s)
        m=len(p)
        def wildcard(s,p,i,j,dp):
            if i<0 and j<0:
                return True
            
            if i>=0 and j<0:
                return False
            
            if j>=0 and i<0:
                return isallstars(p,j)
            
            if dp[i][j]!=-1:
                return dp[i][j]
            
            
            if s[i]==p[j] or p[j]=="?":
                dp[i][j]=wildcard(s,p,i-1,j-1,dp)
                
            elif p[j]=="*":
                
                 dp[i][j]=wildcard(s,p,i,j-1,dp) or wildcard(s,p,i-1,j,dp)
            
            else:
                dp[i][j]=False
                
            return dp[i][j]
            
            
        
        dp=[[-1]*m for i in range(n)]
        return wildcard(s,p,n-1,m-1,dp)