class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        ans=float("inf")
        while l<=r:
            mid=(l+r)//2
            if nums[l]<=nums[mid]:
                ans= min(nums[l],ans)
                l=mid+1
            else:
                ans=min(nums[mid],ans)
                r=mid-1
        return ans
                
                