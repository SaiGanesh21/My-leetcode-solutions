class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        res=0
        while "01" in s:
            res+=1
            s=s.replace("01","10")
        return res
  