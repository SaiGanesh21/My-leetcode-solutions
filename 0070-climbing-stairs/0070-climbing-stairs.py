class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[1]=1
        dp[0]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
        # fibonacci series 0,1,1,2,3,5,8
        # climbing stairs 1,1,2,3,5,8
        # starts form o indexing
            
            
             
    
            
          
        