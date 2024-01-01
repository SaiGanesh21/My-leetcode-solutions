class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l=1
        h=max(nums)
        
        
        while l<=h:
            mid=(l+h)//2
            tot=0
            
            for num in nums:
                tot+=(num-1)//mid
            if tot<=maxOperations:
                h=mid-1
                
            else:
                l=mid+1
                
        return l
    