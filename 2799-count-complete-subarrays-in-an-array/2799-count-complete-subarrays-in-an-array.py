class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        c=0
        m=len(set(nums))
        for i in range(len(nums)):
            s=set()
            for j in range(i,len(nums)):
                s.add(nums[j])
                if len(s)==m:
                    c+=1
        return c
        #        c=0
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         if len(set(nums[i:j+1]))==m:
        #             c+=1
        # return c