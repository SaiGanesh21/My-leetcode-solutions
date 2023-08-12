class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans=[1]*len(nums)
        
        for i in range(len(nums)):
            for j in range(0,i):
                if nums[j]<nums[i]:
                    ans[i]=max(ans[i],1+ans[j])
        return max(ans)