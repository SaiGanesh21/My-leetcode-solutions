class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l=1
        h=max(quantities)
        
        def minpossible(m):
            c=0
            for x in quantities:
                c+=ceil(x/m)
            return c<=n
        
        while l<=h:
            m=(l+h)//2
            if minpossible(m):
                h=m-1
            else:
                l=m+1
        return l
        
          
        