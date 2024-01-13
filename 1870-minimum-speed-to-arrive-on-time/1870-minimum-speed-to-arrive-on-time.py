class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
     
        
        def minpos(m):
            c=0
            n=len(dist)
            for i in range(n-1):
                c+=ceil(dist[i]/m)
            c+=dist[n-1]/m
            return c<=hour
        
        l=1
        r=10**7
        while l<=r:
            m=(l+r)//2
            if minpos(m):
                r=m-1
            else:
                l=m+1
        if minpos(l):
            return l
        return -1