class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
# Must know:

# XOR of a number with 0 is the number itself.
# XOR of a number with itself is 0.
# The rest is bit manipulation based on the above facts:


# 1 << maximbit equals 2 ** maximbit, (1<<maximbit) - 1 gives us a mask, i.e. a number which has a binary representation of maximbit number of ones. This number is the largest number we can get that is less than 2 ** maximbit. In a loop we find the number that when combined with XOR of all numbers would give us maxnum.

# Bitwise left shift: Shifts the bits of the number to the left and fills 0 on voids right as a result. Similar effect as of multiplying the number with some power of two.
# Example 1:
# a = 5 = 0000 0101 (Binary)
# a << 1 = 0000 1010 = 10
# a << 2 = 0001 0100 = 20 

# Example 2:
# b = -10 = 1111 0110 (Binary)
# b << 1 = 1110 1100 = -20
# b << 2 = 1101 1000 = -40 
# 	rxor = 0
# 	for n in nums:
# 		rxor ^= n

# 	maxnum = (1 << maximumBit) - 1
# 	results = []
# 	while nums:
# 		lw = (rxor & maxnum) ^ maxnum
# 		results.append(lw)
		# rxor ^= nums.pop()
    # return results

    
    
            maxi=2**maximumBit-1
            ans=[]
            y=0
            for x in nums:
                y^=x

            while nums: 
                ans.append(maxi^y)
                y^=nums.pop()
            return ans

        
        
        
        
        
        
        
        
        
        
        