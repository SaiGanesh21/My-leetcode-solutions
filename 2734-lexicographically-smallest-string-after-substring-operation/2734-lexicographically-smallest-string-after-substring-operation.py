class Solution:
    def smallestString(self, s: str) -> str:
        s=list(s)
        for i in range(len(s)):
            if s[i]!="a":
                while i<len(s) and s[i]!="a":
                    s[i]=chr(ord(s[i]) - 1)
                    i+=1
                break
        else :
            s[-1]="z"
            
        return (''.join(s))
            