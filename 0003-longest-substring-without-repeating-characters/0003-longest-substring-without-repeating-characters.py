class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setforstoringch=set()
        l=0
        res=0
        for r in range(0,len(s)):
            while s[r] in setforstoringch:
                setforstoringch.remove(s[l])
                l+=1
            setforstoringch.add(s[r])
            res=max(res,r-l+1)
        return res

            
        