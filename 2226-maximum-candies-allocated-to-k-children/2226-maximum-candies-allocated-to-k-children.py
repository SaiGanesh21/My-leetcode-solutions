class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        def ispossible(candies,mid,k):
            candypiles=0
            for x in candies:
                candypiles+=x//mid
            return candypiles>=k
                    
        
        
        l=1
        h=sum(candies)//k
        
        while l<=h:
            mid=(l+h)//2
            
            if ispossible(candies,mid,k):
                l=mid+1
            else:
                h=mid-1
        return h
                
                
                
                