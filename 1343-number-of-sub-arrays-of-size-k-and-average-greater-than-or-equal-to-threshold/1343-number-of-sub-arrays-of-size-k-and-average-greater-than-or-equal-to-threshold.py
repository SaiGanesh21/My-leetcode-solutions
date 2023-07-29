class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        c,j,n=0,0,len(arr)
        s=sum(arr[:k])
        if s/k>=threshold:
            c=1
        for i in range(k,n):
            s+=arr[i]-arr[j]
            if s/k>=threshold:
                c+=1
            j+=1
        return c

#         a=sum(arr[0:k])
#         c=0
#         if a//k>=threshold:
#             c+=1
    
#         for i in range(len(arr)-k):
#             a=a-arr[i]+arr[i+k]
#             if a//k>=threshold:
#                 c+=1
#         print(c)
#         return c
    
#     count = 0
# current_sum = sum(arr[:k])  # 1-st window
# if current_sum / k >= float(threshold): # check for 1-st window
# 	count += 1

# for i in range(len(arr) - k):
# 	current_sum += (-1) * arr[i] + arr[i + k]  # subtract 1-st element of current window & add the k-th
# 	if current_sum / k >= float(threshold):
# 		count += 1
# return count