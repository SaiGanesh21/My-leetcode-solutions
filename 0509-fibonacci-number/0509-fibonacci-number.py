class Solution:
    def fib(self, n: int) -> int:
        # if n==0:
        #     return 0
        # elif n==1:
        #     return 1
        # else:
        #     return self.fib(n-1)+self.fib(n-2)
#         if n==0:
#             return 0
#         dp=[0]*(n+1)
#         dp[1]=1
#         for i in range(2,n+1):
#             dp[i]=dp[i-1]+dp[i-2]
#         return dp[n]
        if n<=1:
            return n
        dp=[-1]*(n+1)
        if dp[n]!=-1:
            return dp[n]
        dp[n]=self.fib(n-1)+self.fib(n-2)
        return dp[n]
        
          
            
            
            