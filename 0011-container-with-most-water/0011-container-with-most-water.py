class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxs=0
        while l<r:
            maxs=max(maxs,(min(height[l],height[r])*(r-l)))
            if height[l]<=height[r]:
                l+=1
            elif height[l]>height[r]:
                r-=1
        return maxs
      