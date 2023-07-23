class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        stack=[nums[-1]]
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<=stack[-1]:
                stack[-1]+=nums[i]
            else:
                stack.pop()
                stack.append(nums[i])
            
        return stack[-1]
            
            