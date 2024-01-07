class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        def ispossible(mid,price,k):
            prev=price[0]
            k1=1
            for i in range(1,len(price)):
                if prev+mid<=price[i]:
                    k1+=1
                    prev=price[i]
            return k1>=k
                    
                    
                
        price.sort()
        n=len(price)
        l=0
        h=price[n-1]-price[0]
        ans=0
        while l<=h:
            mid=(l+h)//2
            if ispossible(mid,price,k):
                # ans=mid
                l=mid+1
            else:
                h=mid-1
        return h
            
        