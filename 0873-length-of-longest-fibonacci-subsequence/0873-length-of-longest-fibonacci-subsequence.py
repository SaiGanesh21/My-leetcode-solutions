class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        s=set(arr)
        m=0
        for l in range(len(arr)-2):
            for r in range(l+1,len(arr)-1):
                res=0
                start=arr[l]
                next1=arr[r]
                next2=start+next1
                while next2 in s:
                    start=next1
                    next1=next2
                    next2=start+next1
                    
                    res+=1
                m=max(res,m)
        if m:
            return m+2
        else:
            return 0
        
        #         n = len(arr)
        # exists = set(arr)
        # res = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         a = arr[i]
        #         b = arr[j]
        #         l = 2
        #         while a + b in exists:
        #             a, b = b, a + b
        #             l += 1
        #         if l > 2:
        #             res = max(res, l)
        # return res
                

                
            
       