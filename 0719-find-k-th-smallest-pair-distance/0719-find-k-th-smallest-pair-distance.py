class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def possible(guess_dist):
            i = count = 0
            j = 1
            while i < len(nums):
                while (j < len(nums)) and ((nums[j] - nums[i]) <= guess_dist):
                    j += 1
                count += j - i - 1
                i += 1
            return count >= k

        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]

        while lo < hi:
            mid = (lo + hi) // 2
            if possible(mid):
                hi = mid
         
            else:
                lo = mid + 1
        return lo
# 9493929218
        def ispossible(mid,nums,k):
            total=0
            j=1
            i=0
            for i in range(len(nums)):
                while (j<len(nums)) and ((nums[j]-nums[i])<=mid):
                    j+=1
                total+=j-i-1
            return total>=k
            
        nums.sort()
        l=0
        h=nums[-1]-nums[0]
        
        while l<h:
            mid=(l+h)//2
            if ispossible(mid,nums,k):
                r=mid
            else:
                l=mid+1
        return l
        
     
            
            
            
            
            
            
            
        
    