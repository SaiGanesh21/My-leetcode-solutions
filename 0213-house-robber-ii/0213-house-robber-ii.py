class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2: return max(nums)
        def robber(nums):
            for i in range(1,len(nums)):
                if i==1:
                    nums[i] =max(nums[i-1],nums[i])
                else:
                    nums[i]=max(nums[i]+nums[i-2],nums[i-1])
            return nums[-1]
        res1=robber(nums[0:len(nums)-1])
        res2=robber(nums[1:len(nums)])
        return max(res1,res2)
        
        
        #    for i in range(1,len(nums)):
        #     if i==1:
        #         nums[i]=max(nums[i],nums[i-1])
        #     else:
        #         nums[i]=max(nums[i-1],nums[i]+nums[i-2])
        # return nums[-1]