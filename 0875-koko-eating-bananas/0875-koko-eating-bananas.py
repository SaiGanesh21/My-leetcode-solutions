class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        
        while l<=r:
            mid=(l+r)//2
            totaltime=0
            for i in range(len(piles)):
                totaltime+=math.ceil(piles[i]/mid)
            if totaltime<=h:
                r=mid-1
            else:
                l=mid+1
        return l
                 
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
      
        
        
        
        
        
        