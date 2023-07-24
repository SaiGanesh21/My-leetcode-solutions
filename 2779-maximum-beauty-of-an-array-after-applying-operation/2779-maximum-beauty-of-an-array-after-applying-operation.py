class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        d=defaultdict(int)
        for x in nums:
            d[x-k]+=1
            d[x+k+1]-=1
            
        prefixsumvaluetimes=0
        maxtimes=0
        for k,v in sorted(d.items()):
            prefixsumvaluetimes+=v
            maxtimes=max(prefixsumvaluetimes,maxtimes)
        return maxtimes
            


#         d = collections.defaultdict(int)
#         for num in nums:
#             d[num - k] += 1
#             d[num + k  + 1] -= 1
        
#         cnt = cur = 0
#         for k, v in sorted(d.items()):
#             cur += v
#             cnt = max(cnt, cur)
        
#         return cnt
