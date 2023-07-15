class Solution:
    def search(self, arr: List[int], k: int) -> int:
        low=0
        n=len(arr)
        high = n - 1
        while low <= high:
            mid = (low + high) // 2

            # if mid points the target
            if arr[mid] == k:
                return mid

            # if left part is sorted
            if arr[low] <= arr[mid]:
                if arr[low] <= k and k <= arr[mid]:
                    # element exists
                    high = mid - 1
                else:
                    # element does not exist
                    low = mid + 1
            else:  # if right part is sorted
                if arr[mid] <= k and k <= arr[high]:
                    # element exists
                    low = mid + 1
                else:
                    # element does not exist
                    high = mid - 1
        return -1

#         l=0
#         r=len(nums)-1
#         while l<=r:
#             mid=(l+r)//2
#             if nums[mid]==target:
#                 return mid
#             # else:
#                 if nums[l]<=nums[mid]:
#                     if nums[l]<=target and target<=nums[mid]:
#                         h=mid-1
#                     else:
#                         l=mid+1
#                 else:
#                     if nums[mid]<=target and target<=nums[r]:
#                         l=mid+1
#                     else:
#                         h=mid-1
#         return -1
               
        
        
        
#         l, r = 0, len(nums) - 1
        
#         while l <= r:
#             mid = (l + r) // 2
#             if target == nums[mid]:
#                 return mid
            
#             # left sorted portion
#             if nums[l] <= nums[mid]:
#                 if target > nums[mid] or target < nums[l]:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
#             # right sorted portion
#             else:
#                 if target < nums[mid] or target > nums[r]:
#                     r = mid - 1
#                 else:
#                     l = mid + 1
#         return -1