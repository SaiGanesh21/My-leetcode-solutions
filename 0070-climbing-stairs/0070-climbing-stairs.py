class Solution:
    def climbStairs(self, n: int) -> int:
        # dp=[0]*(n+1)
        # dp[1]=1
        # dp[0]=1
        # for i in range(2,n+1):
        #     dp[i]=dp[i-1]+dp[i-2]
        # return dp[n]
        # fibonacci series 0,1,1,2,3,5,8
        # climbing stairs 1,1,2,3,5,8
        # starts form o indexing
        if n==0: return 0
        if n==1: return 1
        if n==2: return 2
        dp = [0]*(n+1) # considering zero steps we need n+1 places
        dp[1]= 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] +dp[i-2]
        print(dp)
        return dp[n]

            
            
             
    
            
          
        