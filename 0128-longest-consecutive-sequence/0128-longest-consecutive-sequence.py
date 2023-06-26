class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        m=0
        for x in s:
            res=1
            if x-1 not in s:
                while x+1 in s:
                    res+=1
                    x+=1
                m=max(m,res)
        return m
                
            
