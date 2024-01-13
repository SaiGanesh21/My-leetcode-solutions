class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
#         ans=[1]*len(nums)
        
#         for i in range(len(nums)):
#             for j in range(0,i):
#                 if nums[j]<nums[i]:
#                     ans[i]=max(ans[i],1+ans[j])
#         return max(ans)
    
    
        lis=[1]*len(nums)
        
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[i]>nums[j] and lis[i]<lis[j]+1:
                    lis[i]=lis[j]+1
        return max(lis)

# 	/* Compute optimized LIS values in bottom up manner */
# 	for (int i = 1; i < n; i++ ) 
# 	{ 
# 		lis[i] = 1; 
# 		for (int j = 0; j < i; j++ ) 
# 			if ( arr[i] > arr[j] && lis[i] < lis[j] + 1) 
# 				lis[i] = lis[j] + 1; 
# 	} 

# 	// Return maximum value in lis[] 
# 	return *max_element(lis, lis+n); 