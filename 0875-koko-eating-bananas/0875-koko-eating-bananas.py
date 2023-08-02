class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        
        def time(m):
            c=0
            for x in piles:
                c+=ceil(x/m)
            return c<=h
                
        while l<=r:
            m=(l+r)//2
            
            if time(m):
                r=m-1
            else:
                l=m+1
        return l
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        l=1
        r=max(piles)
        
        while l<r:
            mid=(l+r)//2
            totaltime=0
            for i in range(len(piles)):
                totaltime+=math.ceil(piles[i]/mid)
            if totaltime<=h:
                r=mid-1
            else:
                l=mid+1
        return l
                 
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
      
        
        
        
        
        
        