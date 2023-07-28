class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s=list(map(str,nums))
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if s[i]+s[j]<s[j]+s[i]:
                    s[i],s[j]=s[j],s[i]
                    
        return "".join(s).lstrip("0") or "0"
        
        
