class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
   
        l=1
        r=max(nums)
        
        def thre(m):
            c=0
            for x in nums:
                c+=ceil(x/m)
            return c<=threshold
            
        while l<=r:
            m=(l+r)//2
            if thre(m):
                r=m-1
            else:
                l=m+1
        return l
    
    
     
        
        
        
                
       
    