class Solution:
    def largestPalindromic(self, num: str) -> str:
        c=Counter(num)
        start=[]
        for x in "9876543210":
            if x=="0" and start==[]:
                break
            start.extend([x]*(c[x]//2))
            c[x]=c[x]%2
        center=""
        for x in "9876543210":
            if c[x]:
                center=x
                break
        return "".join(start)+center+"".join(start[::-1])
            
        
            
            
                    
            