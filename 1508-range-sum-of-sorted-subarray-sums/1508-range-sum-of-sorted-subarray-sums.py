class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        l=[]
        for i in range(len(nums)):
            s=0
            for j in range(i,len(nums)):
                s+=nums[j]
                l.append(s)
        l.sort()
        return sum(l[left-1:right])%(10**9+7)
    
                
                
    #          l = []
    # for i in range(len(nums)):
    #     cum = 0
    #     for j in range(i,len(nums)):
    #         cum+=nums[j]
    #         l.append(cum)
    # l.sort()
    # return sum(l[left-1:right])%(10**9+7) 