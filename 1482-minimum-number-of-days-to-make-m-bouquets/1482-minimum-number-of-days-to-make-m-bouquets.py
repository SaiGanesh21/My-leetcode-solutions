class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        val=m*k
        if val>len(bloomDay):
            return -1
        
        def possible(bloomDay,days,m,k):
            numberofbouquets=0
            count=0
            n=len(bloomDay)
            for i in range(n):
                if bloomDay[i]<=days:
                    count+=1
                else:
                    numberofbouquets+=count//k
                    count=0
            numberofbouquets+=count//k
            return numberofbouquets>=m
        
        
        l=min(bloomDay)
        h=max(bloomDay)
        
        while l<=h:
            mid=(l+h)//2
            
            if possible(bloomDay,mid,m,k):
                h=mid-1
            else:
                l=mid+1
        return l