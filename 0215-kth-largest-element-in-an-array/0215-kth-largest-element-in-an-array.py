class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums1=[]
        # p=heapq.heapify(nums)
        # for x in nums:
        #     heapq.heappush(nums1,k)
        # for i in range(k):
        #     c=heapq.heappop(k[i])
        # return -c
        nums=[-x for x in nums]
        heapq.heapify(nums)
        
        while k!=0:
            ans=heapq.heappop(nums)
            k-=1
        return -1*ans
            
        
      
        