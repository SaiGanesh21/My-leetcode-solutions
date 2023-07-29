class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d=defaultdict(int)
        d[0]=1
        prefixsum=0
        c=0
        for x in nums:
            prefixsum+=x
            if prefixsum-k in d:
                c+=d[prefixsum-k]
            d[prefixsum]+=1
        return c
            
        
        