class Solution:
    def partitionString(self, s: str) -> int:
        l=0
        r=len(s)-1
        d=defaultdict(list)
        i=0
        while l<=r:
            while l<=r and s[l] not in d[i]:
                d[i].append(s[l])
                l+=1
            i+=1
        return len(d)
        
                
        