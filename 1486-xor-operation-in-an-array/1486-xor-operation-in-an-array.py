class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[0]*n
        for i in range(n):
            nums[i]=start+2*i
        res=0
        for x in nums:
            res=res^x
        return res
            