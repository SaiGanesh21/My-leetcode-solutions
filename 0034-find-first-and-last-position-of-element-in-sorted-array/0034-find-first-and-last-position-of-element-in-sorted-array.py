class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def firstoccur(nums,target):
            l=0
            h=len(nums)-1
            l1=[]
            first=-1
            while l<=h:
                m=(l+h)//2
                if target==nums[m]:
                    first=m
                    h=m-1
                elif target>nums[m]:
                    l=m+1
                else:
                    h=m-1
            return first
        
        def lastoccur(nums,target):
            l=0
            h=len(nums)-1
            l1=[]
            last=-1
            while l<=h:
                m=(l+h)//2
                if target==nums[m]:
                    last=m
                    l=m+1
                elif target>nums[m]:
                    l=m+1
                else:
                    h=m-1
            return last
        f=firstoccur(nums,target)
        if f==-1:
            return [-1,-1]
        l=lastoccur(nums,target)
        return [f,l]



