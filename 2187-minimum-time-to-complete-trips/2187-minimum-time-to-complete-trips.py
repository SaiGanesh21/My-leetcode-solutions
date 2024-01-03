class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        def ispossible(mid,time,totalTrips):
            trips=0
            for x in time:
                trips+=mid//x
            return trips>=totalTrips
                
        
        l=1
        r=10**14
        
        while l<=r:
            mid=(l+r)//2
            
            if ispossible(mid,time,totalTrips):
                r=mid-1
            else:
                l=mid+1
        return l
        
        
        